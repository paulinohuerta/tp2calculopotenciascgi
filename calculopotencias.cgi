#!/usr/bin/perl
use CGI;
$cgi = new CGI;
print $cgi->header(-charset => 'utf-8');
print $cgi->start_html('Cálculo de potencia');

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
        if($b+0 ne $b or $exp+0 ne $exp) {
          $mens = "Base y exponente deben ser numéricos";
        }
        else {
	  $resultado=1;
	  for(my $i=0;$i<$exp;$i++){
	    $resultado=$resultado*$b;
	  }
          $mens = "El resultado de elevar $b a $exp es $resultado";
        }
	print $cgi->h3($mens);
}
print $cgi->end_html;
