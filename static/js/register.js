<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script type="text/javascript"></script>
</head>

var result = "";
$("input[type=radio]:checked").each(function () {
  result = $(this).val() ;
});