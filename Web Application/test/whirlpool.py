import whirlpool



wp = whirlpool.new("My String")
wp = whirlpool.new(data.encoding('utf-8'))
hashed_string = wp.hexdigest()

wp.update("My Salt")
hashed_string = wp.hexdigest()


