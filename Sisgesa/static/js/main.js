$(document).on('ready', inicio);

function inicio()
{
	$('.submenu_cursos').on('click', mostrarSubmenu);
}

function mostrarSubmenu()
{
	$('#cursos').toggle();
}