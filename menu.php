<html>
<link rel="shortcut icon" href="icon.png">
<head>
<title>Menu Card</title>
</head>
<style type="text/css" >
.heading
{
	text-align: center;
    color: white;
    text-shadow: 2px 2px red;
    padding-top: 5px;
}

.table
{
    color: white;
    text-shadow: 0.5px 0.5px black;
}
    
body
{
    background-color: darkgray;    
}

</style>



<body >
<div class="heading"><h1>Bangalore Delicacy</h1></div>
<div class="table"><?php
    $f1=file_get_contents('./normaldish.txt');
    $normal = explode("$", $f1);
    array_pop($normal);
    $f2=file_get_contents('./special.txt');
    $special = explode("$", $f2);
    array_pop($special);
?>
    <table border="0" cellspacing="20" align="left">
    <tr>
        <td>Food Code</td>
        <td>Food Name</td>
        <td>Food Price</td>
    </tr>
    <?php
    foreach ($normal as &$value)
    {
        $ro=explode("|",$value);
        ?>
        <tr>
        <td><?php echo($ro[0]); ?></td>
        <td><?php echo($ro[1]); ?></td>
        <td><?php echo($ro[2]); ?></td>
        </tr>
        <?php
    }
    ?>
    </table>
    <table border="0" cellspacing="20" align="right">
    <tr>
        <td>Food Code</td>
        <td>Food Name</td>
        <td>Food Price</td>
    </tr>
    <?php
    foreach ($special as &$value)
    {
        $ro=explode("|",$value);
        ?>
        <tr>
        <td><?php echo($ro[0]); ?></td>
        <td><?php echo($ro[1]); ?></td>
        <td><?php echo($ro[2]); ?></td>
        </tr>
        <?php
    }
    ?>
    </table>
</div>
</body>

</html>