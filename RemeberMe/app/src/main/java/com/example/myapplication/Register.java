package com.example.myapplication;

import android.app.DatePickerDialog;
import android.app.Dialog;
import android.content.Context;
import android.content.Intent;
import android.graphics.Color;
import android.os.Bundle;
import android.text.TextUtils;
import android.util.Log;
import android.util.Patterns;
import android.view.View;
import android.view.inputmethod.InputMethodManager;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.DatePicker;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.google.gson.JsonObject;
import com.koushikdutta.async.future.FutureCallback;
import com.koushikdutta.ion.Ion;

import java.util.Calendar;

public class Register extends AppCompatActivity {
    EditText edt;
    int y,m,d;
    EditText edt2;
    EditText edt3;
    TextView t1;
    String pass1;
    String pass2;
    Button b_register;
    static final int DIALOG_ID=0;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);
        final Calendar cal= Calendar.getInstance();
        y=cal.get(Calendar.YEAR);
        m=cal.get(Calendar.MONTH);
        d=cal.get(Calendar.DAY_OF_MONTH);
        showDialogonEditTextClick(); //to show Calendar Dialog Box to select date of birth
        //Spinner begin
//        Spinner mySpinner = (Spinner) findViewById(R.id.spinner2);
        //Spinner End
    }
    public void showDialogonEditTextClick(){
        edt= (EditText)findViewById(R.id.dob);
        edt.setOnClickListener(
                new View.OnClickListener() {
                    @Override
                    public void onClick(View v) {
                        closekeyboard();
                        showDialog(DIALOG_ID);
                    }
                }
        );
    }
    @Override
    protected Dialog onCreateDialog(int id){
        if(id==DIALOG_ID)
            return new DatePickerDialog(this,dpickerListener,y,m,d);
        return null;
    }
    private DatePickerDialog.OnDateSetListener dpickerListener
            = new DatePickerDialog.OnDateSetListener() {
        @Override
        public void onDateSet(DatePicker view, int year, int month, int dayOfMonth) {
            y=year;
           m=month+1;
           d=dayOfMonth;
           closekeyboard();
            edt.setText(d+"/"+m+"/"+y);
            edt.setTextColor(Color.rgb(255,255,224));
            //Toast.makeText(Register.this,y+"/"+m+"/"+d,Toast.LENGTH_LONG).show();
        }
    };
    private void closekeyboard(){
        View view=this.getCurrentFocus();
        int flags;
        if(view!=null){
            InputMethodManager imm=(InputMethodManager)getSystemService(Context.INPUT_METHOD_SERVICE);
            imm.hideSoftInputFromWindow(view.getWindowToken(), flags=0);
        }
    }
    public static boolean isValidEmail(CharSequence target) {
        return (!TextUtils.isEmpty(target) && Patterns.EMAIL_ADDRESS.matcher(target).matches());
    }
    public boolean isValidPassword()
    {
        edt2=(EditText)findViewById(R.id.editText8);
        edt3=(EditText)findViewById(R.id.editText9);
        String p=edt2.getText().toString();
        String p2=edt3.getText().toString();
        return p.equals(p2);
    }
    public void onRegister(View view){
        EditText edt1 = (EditText)findViewById(R.id.editText3);
        String s2=edt1.getText().toString();
        boolean a = isValidEmail(s2);
        boolean b= isValidPassword();
        EditText Fullname = findViewById(R.id.editText4);
        EditText pass = findViewById(R.id.editText8);
        EditText em=findViewById(R.id.editText3);
        EditText user=findViewById(R.id.editText7);
        String fullnme = String.valueOf(Fullname.getText());
        String password = String.valueOf(pass.getText());
        String email= String.valueOf(em.getText());
        final Button bt1 = findViewById(R.id.button);
        String username= String.valueOf(user.getText());

//        tosend.addProperty("email",email);

        if(a && b)
        {
            JsonObject tosend = new JsonObject();
            tosend.addProperty("username",username);
            tosend.addProperty("password",password);
            tosend.addProperty("name",fullnme);
            Ion.with(getApplicationContext())
                    .load("https://remme.herokuapp.com/api/create/user")
                    .setJsonObjectBody(tosend)
                    .asJsonObject()
                    .setCallback(new FutureCallback<JsonObject>() {
                        @Override
                        public void onCompleted(Exception e, JsonObject result) {
                            Log.d("Response",result.toString());
                            if(result.toString().contains("User Created")){
                                startActivity(new Intent(getApplicationContext(),MainActivity.class));
                            }
                            Toast.makeText(getApplicationContext(),result.get("message").toString(),Toast.LENGTH_LONG).show();
                        }

                    });
        }
        else if(!a && (!b||b))
        {
            Toast.makeText(Register.this,"Invalid email", Toast.LENGTH_LONG).show();
        }
        else if(a && !b)
        {
            Toast.makeText(Register.this,"Passwords don't match", Toast.LENGTH_LONG).show();
        }

    }
}
