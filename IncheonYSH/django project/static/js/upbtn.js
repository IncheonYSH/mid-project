

$(function(){
    $(window).on('scroll',function(){
      var scrollBottom = $(document).height() - $(window).height() - $(window).scrollTop();

        if(scrollBottom<=$('#big_footer').height()){
            $('#btn_go_top').addClass('bottom')
        } else {
            $('#btn_go_top').removeClass('bottom')
        }
    });
    $('#btn_go_top').on('click',function(){
        $('html,body').animate({scrollTop:0},500);
    })
});
