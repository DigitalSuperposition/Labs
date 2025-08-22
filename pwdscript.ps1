$server = hqqua22020
$port = 443

for($i=0; $i -le 10; $i++) {
	Test-NetConnection -ComputerName $server -Port $port
}