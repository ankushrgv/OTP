$(document).on('ready', function(){

    $('.right_container').hide();

    $(document).on('click','.string-name', function(event){
        $this = $(this);
        $(document).find('.active_string').removeClass('active_string');

        $this.addClass('active_string');    
    });


    $(document).on('click','.cls_string_name', function(event){            
        var object_id, matches, usergroup;
        
        $this = $(this);

        object_id = $this.attr("id");
        object_string_type = $this.data("string-type");

        $('.right_container').show();
        if(object_string_type == "contacts"){
            populateUserDetails(object_id);
        }
        window.scrollTo(0, 0);
    });    


    $('.send-msg-form').validate({
        
        rules:{
            'msg':{
                required:true,
                minlength:6,
                maxlength:150
            }
        },
        messages:{
            'msg':{
                required:'Message is required',
                minlength:'Message should have atleast 6 characters',
                maxlength:'Message should have less than 150 characters'
            },
        },
        ignore:[],
        onfocusout:function(element) {
            $(element).valid();
        },
        highlight:function(el) {
            $(el).addClass('redborder');
        },

        unhighlight:function(el){
            $(el).removeClass('redborder');
        },
        invalidHandler: function(event, validator) {
            console.log(event);
        },
        submitHandler: function(form){
            send_msg_form_submit();
        }
    });
});


function send_msg_form_submit() {
    console.log("OTP Sent !!");
}


function populateUserDetails(id) {
    var url = "/get_user_details/?s=" + id;
    $.get(url, function(response) {
        $container = $('.details-container');

        var i = 0;

        if (response.length > 0) { 
            $container.html("");
            $container.append("<h5> User Details </h5>");

            var f = document.createDocumentFragment();

            var fm = document.createElement('form');
            $(fm).attr('id','send-msg-form');
            $(fm).attr('action','/send-msg/');
            $(fm).attr('method','GET');

            var d1 = document.createElement('div');
            $(d1).addClass("first-name");
            $(d1).attr('id','first-name');
            
            var e1 = document.createElement('div');
            $(e1).addClass("inner-first-name");
            $(e1).attr('id','inner-first-name');
            $(e1).append("<h3> First Name </h3>");
            
            $(d1).append($(e1));
            $(d1).append("<h3> : </h3>");
            $(d1).append($("<h3 id='first-name-id'>").text(response[0]));
            
            var d2 = document.createElement('div');
            $(d2).addClass("last-name");
            $(d2).attr('id','last-name');

            var e2 = document.createElement('div');
            $(e2).addClass("inner-last-name");
            $(e2).attr('id','inner-last-name');
            $(e2).append("<h3> Last Name </h3>");

            $(d2).append($(e2));
            $(d2).append("<h3> : </h3>");
            $(d2).append($("<h3 id='last-name-name'>").text(response[1]));
            
            var d3 = document.createElement('div');
            $(d3).addClass("ph-number");
            $(d3).attr('id','ph-number');
            
            var e3 = document.createElement('div');
            $(e3).addClass("inner-ph-number");
            $(e3).attr('id','inner-ph-number');
            $(e3).append("<h3> Phone Number </h3>");

            $(d3).append($(e3));
            $(d3).append("<h3> : </h3>");
            $(d3).append($("<h3 id='ph-number-id'>").text(response[2]));


            var d4 = document.createElement('div');
            $(d4).addClass("send-msg");
            $(d4).attr('id','send-msg');
            $(d4).append('<input type="submit" id="send-msg-button" class="send-msg-button" value="Send Message">');


            var d5 = document.createElement('input');
            $(d5).attr('type',"hidden");
            $(d5).addClass("user-id");
            $(d5).attr('id','user-id');
            $(d5).attr('name','user-id');
            $(d5).attr('value',response[3]);

            $(fm).append($(d5));
            $(fm).append($(d4));

            f.appendChild(d1);
            f.appendChild(d2);
            f.appendChild(d3);
            f.appendChild(fm);

            $container.append(f);

             
        } else {
            $container.html("");
            $container.append("<h5>Details Not Found</h5>");
        }
    });
}