<?php
if(isset($_POST['name'])){
    $db = 'trip';
    $server = "localhost";
    $username = "root";
    $password = "";

    $conn = mysqli_connect($server, $username, $password, $db);

    if (!$conn) {
        die("Connection failed: " . mysqli_connect_error());
    }
    //echo "Successfully connected to the db"

    $name = $_POST['name'];
    $gender = $_POST['gender'];
    $age = $_POST['age'];
    $email = $_POST['email'];
    $phone = $_POST['phone'];
    $desc = $_POST['desc'];

    $sql = "INSERT INTO `trip` (`name`, `age`, `gender`, `email`, `phone`, `other`, `dt`) VALUES ('$name', '$age', '$gender', '$email', '$phone', '$desc', current_timestamp());";
    echo $sql;

    if($conn->query($sql) == true) {
        echo "success";
    } 
    else{
        echo "error : $sql <br> $conn->error";
    }
    $conn->close();
}
    ?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to travel form</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>
    <div class="container">
        <h1>Welcome to Goa College of Engineering US Trip form</h1>
        <p> Enter your details to comfirm your participation in the trip</p>
        
        
        <?php
        echo'<p style="color:white; background-color:green">Thanks for submitting your form, see you there!</p>'
        
        ?>
        <form action="index.php" method="POST">
            <input type="text" name="name" id="name" placeholder="Enter your Name">
            <input type="text" name="age" id="age" placeholder="Enter your age">
            <input type="text" name="gender" id="gender" placeholder="Enter your gender">
            <input type="text" name="email" id="email" placeholder="Enter your email">
            <input type="text" name="phone" id="phone" placeholder="Enter your phone">
            <textarea name="desc" id="desc" placeholder="Enter any other information here" cols="80" rows="10"></textarea>
            <button class="btn">Submit</button>
        </form>

    </div>
    <script src="index.js"></script>
</body>

</html>

<!--
trip > Trip

sno - PK int 3 AI
name text
age int 3
gender varchar 8
email text
phone varchar10
other textarea
dt datetime 

heroku login
 cd my-project/
$ git init
$ heroku git:remote -a phptestsite

$ git add .
$ git commit -am "make it better"
$ git push heroku master-->
