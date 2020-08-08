<?php

$ooo = shell_exec('python python/final.py');

?>

<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Here's your analysis</title>
    <!-- CSS only -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" 
    integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" 
    crossorigin="anonymous">

    <!-- JS, Popper.js, and jQuery -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" 
    integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" 
    crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" 
    integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" 
    crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" 
    integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" 
    crossorigin="anonymous"></script>
    <style>
        .jumbotron{
            width: 800px;
            height: 800px;
            margin : 0 auto;
        }
        img{
            width: 500px;
            height: 700px;
        }
        a{
            color:black;
        }
        .navbar{
          background-color: #003153;
        }
        .nav-link:hover::after{
            width: 100%;
            opacity: 1;
        }

        .nav-link::after{
            content: "";
            display: block;
            width: 10%;
            height: 2px;
            background: lime;
            margin: 0 auto;
            margin-top: 2px;
            transition-duration: 0.4s;
            opacity: 0;
        }
        span{
            /* font-family: 'Permanent Marker', cursive; */
            font-family: 'Pacifio', cursive;
        }

        .nav-link{
            color: rgb(255, 251, 212);
        }
        a:hover{
            color: rgb(255, 251, 212);
        }
    </style>
</head>
<body>
<nav class="navbar navbar-light" >
    <a class="navbar-brand" href="#">
      <!-- <img src="bootstrap-solid.svg" width="30" height="30" class="d-inline-block align-top" alt="" loading="lazy"> -->
      <span style="color: rgb(241, 232, 199); font-size: x-large;">Whatsapp Analyser</span>
    </a>
    <ul class="nav justify-content-end">
        <li class="nav-item">
          <a class="nav-link yes" href="index.html">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link yes" href="collaboraters.html" target="_blank">Collaboraters</a>
        </li>
      </ul>
  </nav>

<div>
    <img src="images/user.png" class="rounded float-left" alt="...">
<img src="images/spider.png" class="rounded float-right" alt="...">
</div>
<div>
    <img src="images/month.png" class="rounded float-left" alt="...">
    <img src="images/year.png" class="rounded float-right" alt="...">
</div>
<div>
    <img src="images/days.png" class="rounded float-left" alt="...">
    <img src="images/most.png" class="rounded float-right" alt="...">
</div>
<div>
    <img src="images/senti.png" class="rounded float-left" alt="...">
    <img src="images/sentibar.png" class="rounded float-right" alt="...">
</div>
<div>
    <img src="images/hours.png" class="rounded float-left" alt="hours usage bar">
    <img src="images/word.png" width="500" height="500" class="rounded float-left" alt="wordcloud">
</div>
<div><?php echo $ooo; ?></div>

</body>
</html>
