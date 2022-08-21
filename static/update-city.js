$ = django.jQuery
    $(function (){
        let $state = $("select[id$='state']")
        $state.change(function () {
            $state = $("select[id$='state']").val()
            let $city = $("select[id$='city']")
            $.post("/common/fetch-city-list/",
                {
                    "state": $state,
                    "csrfmiddlewaretoken": csrf_token
                },
                function (data, status) {
                    if (status === "success") {
                        if (data != "False") {
                            $city.empty();
                            let data1
                            data1 = JSON.parse(data)
                            for (const [key, value] of Object.entries(data1)) {
                                $city.append($("<option></option>").attr("value", value).text(key));
                            }
                        }
                    }
                });
               })
    })