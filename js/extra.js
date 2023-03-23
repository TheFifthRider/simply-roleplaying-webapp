$( document ).ready($(function( e ){
  delete Hammer.defaults.cssProps.userSelect;

  var bodyHammer = new Hammer( document.body );
  var navHammer = new Hammer( document.getElementsByClassName("wy-side-scroll")[0] );

  bodyHammer.on( "swiperight", swipeNavIn );
  bodyHammer.on( "swipeleft", swipeNavOut );
  navHammer.on( "swiperight", swipeNavIn );
  navHammer.on( "swipeleft", swipeNavOut );

  function swipeNavIn ( event ){
    $("[data-toggle='wy-nav-shift']").addClass("shift");
    $("[data-toggle='rst-versions']").addClass("shift")
  }

  function swipeNavOut ( event ){
    $("[data-toggle='wy-nav-shift']").removeClass("shift");
    $("[data-toggle='rst-versions']").removeClass("shift")
  }
}));

document.querySelectorAll('.headerlink').forEach(item => {
  item.addEventListener('click', event => {
    navigator.clipboard.writeText(item.href);
  });
})