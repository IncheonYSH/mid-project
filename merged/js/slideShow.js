/**
* slideShow.js
**/


$(function(){
    //이동한 이미지의  index 값 저장(현재보고있는 이미지-현재위치)
    var movedIndex=0;

    //슬라이드 패널을 움직여주는 함수
   function moveSlide(index){
        //전달받은 index 값을 movedIndex에 저장
        movedIndex = index; //전역변수
        //슬라이드 이동
        
        var winwidth = $(window).width();        
        var moveLeft = -(index * winwidth);
        $('#slidePanel').animate({'left':moveLeft},'slow');        
    };

    //prev 버튼 클릭하면 앞으로 이동
    $('#prevButton').on('click',function(){
            //버튼클릭시 보여줘야 할 이미지의  index 결정해서
            if(movedIndex !=0) //0번 인덱스 이미지가 아니라면
                movedIndex = movedIndex - 1; //현재 이미지 이전 이전이미지의 인덱스로 설정
            else
                movedIndex = movedIndex + 3;
            //moveSlide() 호출
            moveSlide(movedIndex);

    });//prev 버튼 종료

    //next버튼 클릭하면 뒤로 이동
    $('#nextButton').on('click',function(){
        if(movedIndex !=3) //마지막 이미지가 아니면
            movedIndex = movedIndex + 1;//다음 이미지 인덱스
        else
            movedIndex = movedIndex - 3;
        //함수 호출
        moveSlide(movedIndex);

    });//next버튼 종료

    //각 컨트롤 버튼에 대해
    $('.controlButton').each(function(index){
        $(this).hover(
            function(){ //마우스 올렸을때 이미지 변경
                $(this).attr('src','image/controlButton2.png');
            },
            function() { //마우스를 뗐을때 이미지 변경
                $(this).attr('src','image/controlButton1.png');
            }
        );

        //클릭했을 때 현재 인덱스 값을 moveSlide() 함수에게 전달
        $(this).on('click',function(){
            moveSlide(index);
        }); //on 종료
    });//each 함수 종료 
       
    $(window).on('resize', function(){
        var left_position = -(movedIndex * $(window).width());
        $('#slidePanel').css('position','absolute');
        $('#slidePanel').css('left',left_position);
    });
});//$(function 종료