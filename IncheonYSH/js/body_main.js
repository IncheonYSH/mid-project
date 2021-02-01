var subscribe = document.getElementById("submit_email");
var subscribe_check = document.getElementById("subscribe_container");

subscribe.addEventListener("click", function(){
    var email_address = document.getElementById("email_input").value;
    var formulaRegex = /[0-9a-zA-Z.-_]+@[0-9a-zA-Z.-_]+\.[a-zA-Z]{2,3}/;
    var email_match = formulaRegex.test(email_address);
    var subscribe_alert = "이메일 주소를 확인해 주세요!";
    if (email_match == true) {
        var subscribe_alert = "구독 확인 메일을 발송했습니다.";
    }

    var result_div = document.createElement("div");
    result_div.appendChild(document.createTextNode(subscribe_alert));
    if(!email_match)
        result_div.classList.add("invalid");
    else
        result_div.classList.add("valid");
    subscribe_check.insertBefore(result_div, subscribe_check.firstChild);
    setTimeout(function(){
        $(".invalid").fadeOut(600);
        $(".valid").fadeOut(600);  
    }, 800);
    setTimeout(function(){
        $("#subscribe_container .valid").remove();
        $("#subscribe_container .invalid").remove();
    }, 1400);
});