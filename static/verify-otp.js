let $ = django.jQuery
    $(function (){
            $("#div_id_otp").hide()
            $("#btn-submit").hide()
            $("#btn-submit-verify-otp").hide()
            $("#btn-sign-up").hide()
        let otp_from_back="";
        $("#btn-submit-get-otp").click(function () {
            let $email = $("#id_email").val()
            console.log($email)
            $.post("/accounts/send-otp/",
                {
                    "email": $email,
                    "csrfmiddlewaretoken": csrf_token
                },
                function (data, status) {
                console.log("hello")
                    if (status === "success") {
                        if (data != "False"){
                            otp_from_back = data;
                            $("#div_id_otp").show()
                            $("#btn-submit-get-otp").hide()
                            $("#btn-submit-verify-otp").show()
                            $("#id_email").prop('readonly', true)
                        }
                    }
                }
            );
               })

        $("#btn-submit-verify-otp").click(function (){
            let user_otp=$("#id_otp").val();
            if (user_otp===otp_from_back){
                $("#div_id_otp").hide()
                $("#btn-submit").show()
                $("#btn-submit-verify-otp").hide()
                $("#btn-sign-up").show()
                document.getElementById("verification_status").innerText = "OTP Verified"
            }
            else{
                document.getElementById("verification_status").innerText = "OTP Incorrect! Retry"
            }
        })

    })