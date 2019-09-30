package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;
import androidx.constraintlayout.widget.ConstraintLayout;

import android.content.Context;
import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.util.JsonReader;
import android.util.Log;
import android.view.View;
import android.view.WindowManager;
import android.view.inputmethod.InputMethodManager;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.google.gson.JsonObject;
import com.koushikdutta.async.future.FutureCallback;
import com.koushikdutta.ion.Ion;

import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.MalformedURLException;
import java.net.URL;
import java.nio.charset.StandardCharsets;

import javax.net.ssl.HttpsURLConnection;

public class MainActivity extends AppCompatActivity {
    ConstraintLayout mainLayout;
    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

// Get your layout set up, this is just an example
        mainLayout = (ConstraintLayout) findViewById(R.id.cl);

        this.getWindow().setSoftInputMode(WindowManager.LayoutParams.SOFT_INPUT_STATE_ALWAYS_HIDDEN);
    }
    public void connect(String Url, String requestType, String Params){
        try {
            URL remme = new URL(Url);
            HttpsURLConnection myconn = (HttpsURLConnection) remme.openConnection();
            myconn.setRequestProperty("User-Agent","Remme-mobile-app");
            if(myconn.getResponseCode()==200){
                Log.d("Connection_Response","Response successful");
                InputStream responseBody = myconn.getInputStream();
                InputStreamReader responseBodyReader = new InputStreamReader(responseBody, StandardCharsets.UTF_8);
                JsonReader jsonReader = new JsonReader(responseBodyReader);
                jsonReader.beginObject();
                while(jsonReader.hasNext()){
                    String msg = jsonReader.nextName();
                    String value = jsonReader.nextString();
                    Log.d("Jsonresponse: ", "\""+msg + "\":" + "\""+value+"\"");
                }
                jsonReader.close();
                myconn.disconnect();
            }
            else{
                Log.d("Connection_Response", String.valueOf(myconn.getResponseCode()));
            }
        }
        catch (Exception e) {
            Log.d("Errorjson","ERror occurred " +e);
            e.printStackTrace();
            }
    }
    public void test(View view) {
        final TextView t1 = findViewById(R.id.tv);
        String temp = "Initializing Connection";
        t1.setText(temp);
        AsyncTask.execute(new Runnable(){
            @Override
            public void run(){
                connect("https://remme.herokuapp.com/api/","GET","NULL");
            }
        });
    }
    public void sendPass(View view){
        InputMethodManager imm = (InputMethodManager)getSystemService(Context.INPUT_METHOD_SERVICE);
        imm.hideSoftInputFromWindow(mainLayout.getWindowToken(), 0);
        final EditText et1 = findViewById(R.id.et1);
        String user = String.valueOf(et1.getText());
        final EditText et2 = findViewById(R.id.editText2);
        String pass = String.valueOf(et2.getText());
        JsonObject t = new JsonObject();
        t.addProperty("username",user);
        t.addProperty("password",pass);
        Log.d("BOB","Build started with" +user+pass);
        Ion.with(getApplicationContext())
                .load("POST","http://remme.herokuapp.com/api/check/pass")
                .setJsonObjectBody(t)
                .asJsonObject()
                .setCallback(new FutureCallback< JsonObject>(){

                    @Override
                    public void onCompleted(Exception e, JsonObject result) {
                        String respo = String.valueOf(result.get("message"));
                        Log.d("Check",respo);
                        if (respo.contains("User Confirmed")){
                            Toast.makeText(getApplicationContext(),"Valid",Toast.LENGTH_LONG).show();
                            Log.d("Response","here");
                            startActivity(new Intent(getApplicationContext(),MainActivity.class));
                        }
                        else if(respo.contains("Password Incorrect"))
                            {
                                Toast.makeText(getApplicationContext(),"Incorrect Password",Toast.LENGTH_LONG).show();
                            }
                        else{
                                Toast.makeText(getApplicationContext(),"Please enter a valid username",Toast.LENGTH_LONG).show();
                                Log.d("Response",respo);
                            }
                    }
                });
    }

    public void openRegister(View view) {
        startActivity(new Intent(getApplicationContext(),Register.class));
    }
}

