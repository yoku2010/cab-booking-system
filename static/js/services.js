$(function(){
  $('#unleash_slider').unleash({
          duration: 700,
        childClassName: '.box',
        captionClassName: '.caption',
                SliderWidth: '934px',
                SliderHeight: '350px',
                width: 600,
                Event: "hover",
                CollapseOnMouseLeave: true,
                CaptionAnimation: "opacity"
  });
  $('#faq').dltoggle();
  $("#open").click(function(event){
      $('#faq').dltoggle_show();
      return false;
  });
  $("#close").click(function(event){
      $('#faq').dltoggle_hide();
      return false;
  });
    $('.bwWrapper').BlackAndWhite({
        hoverEffect : true,
        webworkerPath : false,
        responsive:true,
        invertHoverEffect:false
    });
});