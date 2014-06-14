$(function(){
    $('#obo_slider').oneByOne({
    className: 'oneByOne1',              
    easeType: 'random',
    slideShow: true
  });  
  $('.clients_slider').bxSlider({
    auto: false,
    controls : false,
    mode: 'fade',
    pager: true
  }); 
    $('.bwWrapper').BlackAndWhite({
        hoverEffect : true,
        webworkerPath : false,
        responsive:true,
        invertHoverEffect:false
    });
})