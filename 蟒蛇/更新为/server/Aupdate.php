<?php
//非常简单，放在服务端
$O_passwd = '密码';
$Sever_time = time();
$K_time = $_POST['time'];
$K_file_content = $_POST['file_content'];
$K_file_name = $_POST['file_name'];

$K_token = $_POST['token'];
//基本变量准备好
if(abs($Sever_time - $K_time) < 120){
    $Sever_token = md5($K_time.$K_file_name.$O_passwd.$K_file_content);
    if($Sever_token == $K_token){
        $files = fopen($K_file_name,'w');
        fwrite($files,$K_file_content);
        fclose($files);
        echo "OKAY";
    }else{
        echo "ERR".$Sever_token.'/'.$K_token;
    }
    
}


?>
