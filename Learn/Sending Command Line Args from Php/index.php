<?php   

$out = shell_exec('python newscript.py "Hi from Php!"');
echo("<pre>".$out."</pre>");

?>
