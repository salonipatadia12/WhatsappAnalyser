<?php

ini_set('upload_max_filesize', '10M');
ini_set('post_max_size', '10M');
ini_set('max_input_time', 300);
ini_set('max_execution_time', 300);

$host = "localhost"; /* Host name */
$user = "root"; /* User */
$password = ""; /* Password */
$dbname = "whatsapp"; /* Database name */

$con = mysqli_connect($host, $user, $password,$dbname,"3308");
// Check connection
if (!$con) {
  die("Connection failed: " . mysqli_connect_error());
}


//include("config.php");
 
if(isset($_POST['but_upload'])){

  
  $name = $_FILES['fileselect']['name'];
  $target_dir = "upload/";
  $target_file = $target_dir . basename($_FILES["fileselect"]["name"]);

  // Select file type
  $textFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));

  // Valid file extensions
  $extensions_arr = array("txt");

  // Check extension
  if( in_array($textFileType,$extensions_arr) ){
      
      // Convert to base64 
      $text_base64 = base64_encode(file_get_contents($_FILES['fileselect']['tmp_name']));
     $text = 'data:text/'.$textFileType.';base64,'.$text_base64;
      // Insert record
     $query = "insert into chats(name,text) values('".$name."','".$text."')";
     
     mysqli_query($con,$query) or die(mysqli_error($con));
      
      // Upload file
     // echo realpath($name);
     move_uploaded_file($_FILES['fileselect']['tmp_name'],'upload/'.$name);
      //echo "<script>alert('Analyzing the chats..... This may take some time ')</script>";


      echo "<script>window.location.href='analysis.php'</script>";

    }


}

else{
  echo "<script>alert('Go and select a file first.')</script>";
  echo "<script>window.location.href='analyse.html'</script>";
}


?>