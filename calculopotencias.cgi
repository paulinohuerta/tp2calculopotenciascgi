#!/usr/bin/perl
use CGI;
$cgi = new CGI;
print $cgi->header;
print $cgi->start_html('titulo');

if(!$cgi->param){
	print $cgi->start_form;
	print $cgi->h4('Introduce la base:');
	print $cgi->textfield(-name=>'base',-size=>2);
	print $cgi->h4('Introduce el exponente:');
	print $cgi->textfield(-name=>'exponente',-size=>2);
	print $cgi->br;
	print $cgi->br;
	print $cgi->submit(-value=>'Calcula');
	print $cgi->end_form;

}else{
	$b=$cgi->param('base');
	$exp= $cgi->param('exponente');
	$resultado=1;
		for(my $i=0;$i<$exp;$i++){
			$resultado=$resultado*$b;
		}
	print $cgi->h3('El resultado de elevar '.$b.' a '.$exp.' es '.$resultado);
}
print $cgi->end_html;
