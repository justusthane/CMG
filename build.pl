#!/usr/bin/perl
use strict;
use warnings;
use feature qw(say);
use Data::Dumper;
#use Text::Markup::Markdown;
use YAML::PP;
my $ypp = YAML::PP->new;

#my $html = Text::Markup->new->parse(file => 'menu.md');
my %menu = $ypp->load_file("menu.yaml");


open my $fh, ">", "index.html";
my $html = <<~EoF;
	<html>
	<head>
	<title>Cocktail Menu</title>
	<link rel="stylsheet" href="style.css">
	</head>
	<body>
	EoF

$html .= "Hi";

#say Dumper(@menu);
say "Menu";
say Dumper($menu{menu});

print $fh $html;


say $html;
