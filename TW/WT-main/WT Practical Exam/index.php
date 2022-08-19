<?php
    if(isset($_POST['submit'])){
        $string = $_POST['string'];
        $reverse_string = strrev($string);

        print '<scirpt>
            var myVar;
            myVar = "'.$reverse_string.'"
            alert(myVar);
            </script>';
    }
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test Document</title>
</head>
<body>
    <form action="index.php" method="post">
        <p>Enter String: <input type="text" name="string" id="string"></p>
        <input type="submit" value="Reverse String" name="submit">
    </form>
</body>
</html>