
let pop_up_container = document.getElementById('pop-up-container');
let pop_up = document.getElementById('pop-up');
function openpopup()
{
    pop_up_container.style.display="block";
    pop_up.classList.add("open_pop_up");
}
function signout()
{
    window.location = "/logout";
    pop_up_container.style.display="none";
}
function closepopup()
{
    pop_up_container.style.display="none";
    pop_up.classList.remove('open_pop_up');
}


//The flash message:
let flash0 = document.getElementById('flash0');
function hide_flash()
{
    flash0.style.display="none";
}
let delivery = document.getElementById('delivery');

//spinning up the logo icon:
let logo_icon = document.getElementById('logo_icon');
window.onload = function(){
    logo_icon.style.rotate = "360deg";
}

// Some of media query things for small screens:
let MM = window.matchMedia("(max-width: 419px)");
let MMM = window.matchMedia("(max-width: 299px)");
let med991 = window.matchMedia("(max-width: 991px)");
let NEW_ARRIVALS = document.getElementById('NEW_ARRIVALS');
let BEST_SELLERS = document.getElementById('BEST_SELLERS');
let SUB_KIDS = document.getElementById('sub_kids');
let before = window.getComputedStyle(SUB_KIDS, '::before');
if(MM.matches){
    NEW_ARRIVALS.innerText='Arrivals';
    BEST_SELLERS.innerText='Sellers';
    SUB_KIDS.style.left = '-26px';
    SUB_KIDS.style.width = '245px';
}

if(MMM.matches){
    SUB_KIDS.style.left = '-45px';
    SUB_KIDS.style.width = '248px';
    SUB_KIDS.style.setProperty('--beforeLeft', '59px');
}

let show_media_card_btn = document.getElementById('show_media_card_btn');
let media_card_content_div = document.getElementById('media_card_content_div');
let media_card_content_div2 = document.getElementById('media_card_content_div2');
let media_payment_form = document.getElementById('media_payment_form');
let btn_arrow_imgg = document.getElementById('btn_arrow_imgg');
let fast_delivery = document.getElementById('fast_delivery');

if (delivery || fast_delivery){
    function show_med_card(){
        if(media_card_content_div.style.display == "none"){
            media_card_content_div.style.display = "flex";
            btn_arrow_imgg.style.transform = "rotate(180deg)";
        }else{
            media_card_content_div.style.display = "none";
            btn_arrow_imgg.style.transform = "rotate(360deg)";
        }

    }
    show_med_card()
}

// product page and shopping cart:
let product_name = document.getElementById('product_name');
let brand = document.getElementById('brand');
let price_before = document.getElementById('price_before');
let price_after = document.getElementById('price_after');
let size = document.getElementById('size');
let colors_div = document.getElementById('colors_div');
let color1_btn = document.getElementById('color1_btn');
let color2_btn = document.getElementById('color2_btn');
let color3_btn = document.getElementById('color3_btn');
let color4_btn = document.getElementById('color4_btn');
let color5_btn = document.getElementById('color5_btn');
let color_take = document.getElementById('color_take');
let pro_page_content = document.getElementById('pro_page_content');
let quantity = document.getElementById('Quantity');
let add_to_cart_btn = document.getElementById('add_to_cart');
let side_cart_div = document.getElementById('side_cart_div');
let side_cart_div2 = document.getElementById('side_cart_div2');
let cart_pro_name_brand = document.getElementById('cart_pro_name_brand');
let cart_price = document.getElementById('cart_price');
let cart_color_btn = document.getElementById('cart_color_btn');
let cart_size = document.getElementById('cart_size');
let cart_quantity = document.getElementById('cart_quantity');
let cart_img = document.getElementById('cart_img');
let shopping_car = document.getElementById('shopping_car');
let shopping_car2 = document.getElementById('shopping_car2');
let side_cart_product = document.getElementById('side_cart_product');
let size_input = document.getElementById('size_input');
// let total_price = document.getElementById('total_price');
let cartt_delete = document.getElementById('car_delete');
// total += parseFloat(cart_price.innerHTML);
// total_price.innerHTML = "Total Price: "+total;
let cardiv = document.getElementsByClassName("side_cart_div")[0];
let shopping_car_counter = document.getElementById('shopping_car_counter');

let women = document.getElementById('women');
let car_delete_btn = document.getElementById('car_delete_btn');

let size_take = document.getElementById('size_take');
let size_take1 = document.getElementById('size_take1');
let size_take2 = document.getElementById('size_take2');
let color_take2 = document.getElementById('color_take2');
let quantity_take = document.getElementById('quantity_take');
let small = document.getElementById('Small');
let medium = document.getElementById('Medium');
let large = document.getElementById('Large');
let xlarge = document.getElementById('xLarge');
let xxlarge = document.getElementById('xxLarge');
let checkout = document.getElementById('checkout1');
let cart_close_btn = document.getElementById('close_btn');

let i_can_see_you = document.getElementById('i_can_see_you');







window.onscroll = function()
{
    let hide_nav1 = document.getElementById('small_nav');
    let hide_nav2 = document.getElementById('med_nav');
    let hide_nav3 = document.getElementById('the_nav2');
    let the_nav = document.getElementById('the_nav');
    let P = document.getElementById('P');
    let M = window.matchMedia("(max-width: 1100px)");
    let creativeness = document.getElementById('crt');
    let mall = document.getElementById('mall');
    let msg_red = document.getElementById('msg_red');
    let scroll = scrollY + 150;
    let Wscroll = scrollY;

    if(scrollY >= 150 && scrollY <= 880){
        if(i_can_see_you.style.transform == "scale(0)"){
            i_can_see_you.style.transform = "scale(1)";
            setInterval(function(){
                i_can_see_you.style.transform = "scale(0)";
            },5000);
        }
    }else{
        if(i_can_see_you.style.transform == "scale(0)"){
            i_can_see_you.style.transform = "scale(0)";
        }else{
            i_can_see_you.style.transform = "scale(0)"
        }
    }

    shopping_car.onclick = function(){
        if(side_cart_div){
            if(side_cart_div.style.transform == 'scale(0)'){

                side_cart_div.style.transform = 'scale(1)';

                side_cart_div.style.right = "0";
                if(scroll >= 350){
                    side_cart_div.style.top = scroll + 'px'; //250px
                }else{
                    side_cart_div.style.top = '250px'; //250px
                }

            }else{
                side_cart_div.style.transform = 'scale(1)';

                side_cart_div.style.right = "0";

                if(scroll >= 350){
                    side_cart_div.style.top = scroll + 'px'; //250px
                }else{
                    side_cart_div.style.top = '250px'; //250px
                }
            }

        }

        if(side_cart_div2){
            if(side_cart_div2.style.transform == 'scale(1)'){

                side_cart_div2.style.transform = 'scale(0)';

                side_cart_div2.style.right = '-165px';

                side_cart_div2.style.top =  '100px'; // 100px

            }else{


                side_cart_div2.style.transform = 'scale(1)';

                side_cart_div2.style.right = "0";

                side_cart_div2.style.top = '250px';
            }
        }

    }

    shopping_car2.onclick = function(){
        if(side_cart_div){
            if(side_cart_div.style.transform == 'scale(0)'){

                side_cart_div.style.transform = 'scale(1)';

                side_cart_div.style.right = "0";

                if(scroll >= 350){
                    side_cart_div.style.top = scroll + 'px'; //250px
                }else{
                    side_cart_div.style.top = '250px'; //250px
                }
            }else{
                side_cart_div.style.transform = 'scale(1)';

                side_cart_div.style.right = "0";

                if(scroll >= 350){
                    side_cart_div.style.top = scroll + 'px'; //250px
                }else{
                    side_cart_div.style.top = '250px'; //250px
                }
            }

        }

        if(side_cart_div2){
            if(side_cart_div2.style.transform == 'scale(1)'){

                side_cart_div2.style.transform = 'scale(0)';

                side_cart_div2.style.right = '-165px';

                side_cart_div2.style.top = '100px'; //100px

            }else{


                side_cart_div2.style.transform = 'scale(1)';

                side_cart_div2.style.right = "0";

                side_cart_div2.style.top = '250px'; //250px
            }
        }

    }

    if(cart_close_btn)
    {
        cart_close_btn.onclick = function(){
            if(side_cart_div.style.transform == 'scale(1)'){

                side_cart_div.style.transform = 'scale(0)';

                side_cart_div.style.right = '-165px';

                side_cart_div.style.top = '100px';
        }

      }
    }


    if(checkout)
    {
        shopping_car.onclick = function(){
            if(side_cart_div){
                if(side_cart_div.style.transform == 'scale(0)'){

                    side_cart_div.style.transform = 'scale(1)';

                    side_cart_div.style.right = '0px';

                    if(scroll >= 350){
                        side_cart_div.style.top = Wscroll + 'px'; //100px
                    }else{
                        side_cart_div.style.top = '15px'; //100px
                    }
                }else{


                    side_cart_div.style.transform = 'scale(1)';

                    side_cart_div.style.right = "0";

                    if(scroll >= 350){
                        side_cart_div.style.top = Wscroll + 'px'; //15px
                    }else{
                        side_cart_div.style.top = '15px'; //15px
                    }
                }
            }

            if(side_cart_div2){
                if(side_cart_div2.style.transform == 'scale(1)'){

                    side_cart_div2.style.transform = 'scale(0)';

                    side_cart_div2.style.right = '-165px';

                    side_cart_div2.style.top = '250px'; //100px

                }else{


                    side_cart_div2.style.transform = 'scale(1)';

                    side_cart_div2.style.right = "0";

                    if(scroll >= 350){
                        side_cart_div.style.top = Wscroll + 'px'; //100px
                    }else{
                        side_cart_div.style.top = '50px'; //100px
                    }
                }
            }
        }
    }

    if(women)
    {
        shopping_car.onclick = function(){
            if(side_cart_div){
                if(side_cart_div.style.transform == 'scale(0)'){

                    side_cart_div.style.transform = 'scale(1)';

                    side_cart_div.style.right = "0";

                    if(scroll >= 350){
                        side_cart_div.style.top = Wscroll + 'px'; //70px
                    }else{
                        side_cart_div.style.top = '70px'; //70px
                    }

                }else{


                    side_cart_div.style.transform = 'scale(1)';

                    side_cart_div.style.right = "0";

                    if(scroll >= 350){
                        side_cart_div.style.top = Wscroll + 'px'; //70px
                    }else{
                        side_cart_div.style.top = '70px'; //70px
                    }
                }
            }
            if(side_cart_div2){
                if(side_cart_div2.style.transform == 'scale(1)'){

                    side_cart_div2.style.transform = 'scale(0)';

                    side_cart_div2.style.right = '-165px';

                    side_cart_div2.style.top = '100px';

                }else{


                    side_cart_div2.style.transform = 'scale(1)';

                    side_cart_div2.style.right = "0";

                    side_cart_div2.style.top = '250px';
                }
            }
        }
    }

    if (scrollY >= 115 && !delivery)
    {


        if(M.matches){
            the_nav.style.display='none';
            hide_nav3.style.display='none';
            hide_nav1.style.display='none';
            hide_nav2.style.display='none';
            creativeness.style.transition='.9s ease';
            creativeness.style.transform='scale(1.1)';
            mall.style.transition='.9s ease';
            mall.style.transform='scale(1.1)';
        }else{
            the_nav.style.display='flex';
            hide_nav1.style.display='none';
            hide_nav2.style.display='none';
            creativeness.style.transition='.9s ease';
            creativeness.style.transform='scale(1.1)';
            mall.style.transition='.9s ease';
            mall.style.transform='scale(1.1)';
        }
    }
    else
    {
        if(M.matches){
            the_nav.style.display='none';
            hide_nav3.style.display='flex';

            hide_nav1.style.display='flex';
            hide_nav2.style.display='flex';
            creativeness.style.transition='.9s ease';
            creativeness.style.transform='scale(1)';
            mall.style.transition='.9s ease';
            mall.style.transform='scale(1)';
        }else{
            hide_nav3.style.display='none';
            the_nav.style.display='flex';

            hide_nav1.style.display='flex';
            hide_nav2.style.display='flex';
            creativeness.style.transition='.9s ease';
            creativeness.style.transform='scale(1)';
            mall.style.transition='.9s ease';
            mall.style.transform='scale(1)';
        }




    }
    scrollFunction()
}


shopping_car.onclick = function(){
    if(side_cart_div){
        if(side_cart_div.style.transform == 'scale(0)'){

            side_cart_div.style.transform = 'scale(1)';

            side_cart_div.style.right = "0";

            side_cart_div.style.top = '250px'; //250px
        }else{
            side_cart_div.style.transform = 'scale(1)';

            side_cart_div.style.right = "0";

            side_cart_div.style.top = '250px';
        }

    }

    if(side_cart_div2){
        if(side_cart_div2.style.transform == 'scale(1)'){

            side_cart_div2.style.transform = 'scale(0)';

            side_cart_div2.style.right = '-165px';

            side_cart_div2.style.top =  '100px'; // 100px

        }else{


            side_cart_div2.style.transform = 'scale(1)';

            side_cart_div2.style.right = "0";

            side_cart_div2.style.top = '250px';
        }
    }

}

shopping_car2.onclick = function(){
    if(side_cart_div){
        if(side_cart_div.style.transform == 'scale(0)'){

            side_cart_div.style.transform = 'scale(1)';

            side_cart_div.style.right = "0";

            side_cart_div.style.top = '250px';
        }else{
            side_cart_div.style.transform = 'scale(1)';

            side_cart_div.style.right = "0";

            side_cart_div.style.top = '250px';
        }

    }

    if(side_cart_div2){
        if(side_cart_div2.style.transform == 'scale(1)'){

            side_cart_div2.style.transform = 'scale(0)';

            side_cart_div2.style.right = '-165px';

            side_cart_div2.style.top = '100px';

        }else{


            side_cart_div2.style.transform = 'scale(1)';

            side_cart_div2.style.right = "0";

            side_cart_div2.style.top = '250px';
        }
    }

}

if(cart_close_btn)
{
    cart_close_btn.onclick = function(){
        if(side_cart_div.style.transform == 'scale(1)'){

            side_cart_div.style.transform = 'scale(0)';

            side_cart_div.style.right = '-165px';

            side_cart_div.style.top = '100px';
    }

  }
}


if(checkout)
{
    shopping_car.onclick = function(){
        if(side_cart_div){
            if(side_cart_div.style.transform == 'scale(1)'){

                side_cart_div.style.transform = 'scale(0)';

                side_cart_div.style.right = '-165px';

                side_cart_div.style.top = '100px'; //100px

            }else{


                side_cart_div.style.transform = 'scale(1)';

                side_cart_div.style.right = "0";

                side_cart_div.style.top = '15px';
            }
        }

        if(side_cart_div2){
            if(side_cart_div2.style.transform == 'scale(1)'){

                side_cart_div2.style.transform = 'scale(0)';

                side_cart_div2.style.right = '-165px';

                side_cart_div2.style.top = '100px';

            }else{


                side_cart_div2.style.transform = 'scale(1)';

                side_cart_div2.style.right = "0";

                side_cart_div2.style.top = '15px';
            }
        }

    }
}

if(women)
{
    shopping_car.onclick = function(){
        if(side_cart_div){
            if(side_cart_div.style.transform == 'scale(0)'){

                side_cart_div.style.transform = 'scale(1)';

                side_cart_div.style.right = "0";

                side_cart_div.style.top = '70px'; //70px

            }else{


                side_cart_div.style.transform = 'scale(1)';

                side_cart_div.style.right = "0";

                side_cart_div.style.top = '70px';
            }
        }
        if(side_cart_div2){
            if(side_cart_div2.style.transform == 'scale(1)'){

                side_cart_div2.style.transform = 'scale(0)';

                side_cart_div2.style.right = '-165px';

                side_cart_div2.style.top = '100px';

            }else{


                side_cart_div2.style.transform = 'scale(1)';

                side_cart_div2.style.right = "0";

                side_cart_div2.style.top = '250px';
            }
        }

    }
}


//Creating Go up button functions:
let go_up_btn_div = document.getElementById('go_up_btn_div');
let go_up_img = document.getElementById('go_up_img');

function scrollFunction() {
  if (document.body.scrollTop > 640 || document.documentElement.scrollTop > 640) {
    // go_up_btn_div.style.display = "flex";
    go_up_btn_div.style.background = "#00000052";
    go_up_btn_div.style.zIndex = "9999";
    go_up_btn_div.style.boxShadow = "0px 10px 10px rgba(1 1 1 / 65%)"
    go_up_img.style.width = "80%";
    go_up_img.style.height = "90%";
  } else {
    // go_up_btn_div.style.display = "none";
    go_up_btn_div.style.background = "transparent";
    go_up_btn_div.style.zIndex = "0";
    go_up_btn_div.style.boxShadow = "0px 0px 0px rgba(1 1 1 / 65%)";
    go_up_img.style.width = "0";
    go_up_img.style.height = "0";
  }
}
// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
  }

go_up_btn_div.addEventListener("mouseover", () => {
    go_up_btn_div.style.background = "#00000079";
})
go_up_btn_div.addEventListener("mouseout", () => {
    go_up_btn_div.style.background = "#00000052";
})

//categories:
let hidden1 = document.getElementsByClassName("hidden")[0]
let hidden2 = document.getElementsByClassName("hidden")[1]
let hidden3 = document.getElementsByClassName("hidden")[2]
let hidden4 = document.getElementsByClassName("hidden")[3]
let hidden5 = document.getElementsByClassName("hidden")[4]
let show_btn1 = document.getElementsByClassName("show_me")[0];
let show_btn2 = document.getElementsByClassName("show_me")[1];
let show_btn3 = document.getElementsByClassName("show_me")[2];
let show_btn4 = document.getElementsByClassName("show_me")[3];
let show_btn5 = document.getElementsByClassName("show_me")[4];
if(show_btn1){
     function show_btnn1(){
        if ( hidden1.style.display == "none" )
        {
            hidden1.style.display = "block";
        }
        else
        {
            hidden1.style.display = "none";
        }
    };
    show_btnn1()
}

if(show_btn2){
    function show_btnn2(){
        if ( hidden2.style.display == "none" )
        {
            hidden2.style.display = "block";
        }
        else
        {
            hidden2.style.display = "none";
        }
    };
    show_btnn2()
}
if(show_btn3){
    function show_btnn3(){
        if ( hidden3.style.display == "none" )
        {
            hidden3.style.display = "block";
        }
        else
        {
            hidden3.style.display = "none";
        }
    };
    show_btnn3()
}
if(show_btn4){
    function show_btnn4(){
        if ( hidden4.style.display == "none" )
        {
            hidden4.style.display = "block";
        }
        else
        {
            hidden4.style.display = "none";
        }
    };
    show_btnn4()
}
if(show_btn5){
    function show_btnn5(){
        if ( hidden5.style.display == "none" )
        {
            hidden5.style.display = "block";
        }
        else
        {
            hidden5.style.display = "none";
        }
    };
    show_btnn5()
}



//cruds:
let colorss = document.getElementById('colorss');
let add_new_product_here_btn_women;
let create_btn = document.getElementById('create_btn');
let women_cards = document.getElementById('cards_women');
let themes_container = document.getElementById('themes_container');
let new_product_title = document.getElementById('new_product_Title');
let new_product_description = document.getElementById('new_product_description');
let new_product_old_price = document.getElementById('new_product_old_price');
let new_product_new_price = document.getElementById('new_product_new_price');
let new_product_colors = document.getElementById('new_product_colors');
let product_image1 = document.getElementById('product_image1');
let product_image2 = document.getElementById('product_image2');
let product_image3 = document.getElementById('product_image3');
let product_image4 = document.getElementById('product_image4');
let product_image5 = document.getElementById('product_image5');
let product_submit = document.getElementById('product_submit');
let upload_btn1 = document.getElementById('uploadbtn');
let upload_btn2 = document.getElementById('uploadbtn2');
let upload_btn3 = document.getElementById('uploadbtn3');
let upload_btn4 = document.getElementById('uploadbtn4');
let upload_btn5 = document.getElementById('uploadbtn5');
let uploadbtn1_label1 = document.getElementById('uploadbtn_label1');
let uploadbtn2_label2 = document.getElementById('uploadbtn_label2');
let uploadbtn3_label3 = document.getElementById('uploadbtn_label3');
let uploadbtn4_label4 = document.getElementById('uploadbtn_label4');
let uploadbtn5_label5 = document.getElementById('uploadbtn_label5');
let owner = document.getElementById('owner');
let controll_pad= document.getElementById('controll_pad');
let mood = 'create';
let tmp;


let creation = document.getElementById('creation');
let Update_page = document.getElementById('Update_page');
let table = document.getElementById('table');
let tools = document.getElementById('tools');
let process_lap = document.getElementById('process_lap');
let Container = document.getElementById('Container');


// show the image path:
if(owner){
    if(creation || Update_page){

        upload_btn1.onchange = function(){
            product_image1.value = "static/uploads/"+upload_btn1.files[0].name;
        }
        upload_btn2.onchange = function(){
            product_image2.value = "static/uploads/"+upload_btn2.files[0].name;
        }
        upload_btn3.onchange = function(){
            product_image3.value = "static/uploads/"+upload_btn3.files[0].name;
        }
        upload_btn4.onchange = function(){
            product_image4.value = "static/uploads/"+upload_btn4.files[0].name;
        }
        upload_btn5.onchange = function(){
            product_image5.value = "static/uploads/"+upload_btn5.files[0].name;
        }
    }

}









let fast = document.getElementById('fast');
let ml = document.getElementById('ml');
let size_take3 = document.getElementById('size_take3');

if(colorss || fast){
    if(small){
        small.onclick = function(){
            size_take1.value = small.value;
        }
    }
    if(medium){
        medium.onclick = function(){
            size_take1.value = medium.value;
        }
    }
    if(large){
        large.onclick = function(){
            size_take1.value = large.value;
        }
    }
    if(xlarge){
        xlarge.onclick = function(){
            size_take2.value = xlarge.value;
        }
    }
    if(xxlarge){
        xxlarge.onclick = function(){
            size_take2.value = xxlarge.value;
        }
    }
    if(ml){
        ml.onclick = function(){
            size_take3.value = ml.value;
        }
    }

    function fast_check(){

        size_take.value = size_take1.value;
        color_take2.value = color_take.value;
        quantity_take.value = quantity.value;
    }



    if(color1_btn){
        color1_btn.onclick = function(){

            color1_btn.style.width = '35px';
            color1_btn.style.height = '35px';
            color1_btn.style.border = '5px solid black'
            if(color2_btn){
                color2_btn.style.width = '30px';
                color2_btn.style.height = '30px';
                color2_btn.style.border = '3px #c5c3c3ca solid';
            }
            if(color3_btn){
                color3_btn.style.width = '30px';
                color3_btn.style.height = '30px';
                color3_btn.style.border = '3px #c5c3c3ca solid';
            }
            if(color4_btn){
                color4_btn.style.width = '30px';
                color4_btn.style.height = '30px';
                color4_btn.style.border = '3px #c5c3c3ca solid';
            }
            if(color5_btn){
                color5_btn.style.width = '30px';
                color5_btn.style.height = '30px';
                color5_btn.style.border = '3px #c5c3c3ca solid';
            }

            color_take.value = color1_btn.value
        }
    }
    if(color2_btn){
        color2_btn.onclick = function(){
            if(color1_btn){
                color1_btn.style.width = '30px';
                color1_btn.style.height = '30px';
                color1_btn.style.border = '3px #c5c3c3ca solid';
            }

            color2_btn.style.width = '35px';
            color2_btn.style.height = '35px';
            color2_btn.style.border = '5px solid black'
            if(color3_btn){
                color3_btn.style.width = '30px';
                color3_btn.style.height = '30px';
                color3_btn.style.border = '3px #c5c3c3ca solid';
            }
            if(color4_btn){
                color4_btn.style.width = '30px';
                color4_btn.style.height = '30px';
                color4_btn.style.border = '3px #c5c3c3ca solid';
            }
            if(color5_btn){
                color5_btn.style.width = '30px';
                color5_btn.style.height = '30px';
                color5_btn.style.border = '3px #c5c3c3ca solid';
            }

            color_take.value = color2_btn.value;
        }
    }
    if(color3_btn){
        color3_btn.onclick = function(){
            if(color1_btn){
                color1_btn.style.width = '30px';
                color1_btn.style.height = '30px';
                color1_btn.style.border = '3px #c5c3c3ca solid';
            }
            if(color2_btn){
                color2_btn.style.width = '30px';
                color2_btn.style.height = '30px';
                color2_btn.style.border = '3px #c5c3c3ca solid';
            }
            color3_btn.style.width = '35px';
            color3_btn.style.height = '35px';
            color3_btn.style.border = '5px solid black'
            if(color4_btn){
                color4_btn.style.width = '30px';
                color4_btn.style.height = '30px';
                color4_btn.style.border = '3px #c5c3c3ca solid';
            }
            if(color5_btn){
                color5_btn.style.width = '30px';
                color5_btn.style.height = '30px';
                color5_btn.style.border = '3px #c5c3c3ca solid';
            }

            color_take.value = color3_btn.value;
        }
    }
    if(color4_btn){
        color4_btn.onclick = function(){
            if(color1_btn){
                color1_btn.style.width = '30px';
                color1_btn.style.height = '30px';
                color1_btn.style.border = '3px #c5c3c3ca solid';
            }
            if(color2_btn){
                color2_btn.style.width = '30px';
                color2_btn.style.height = '30px';
                color2_btn.style.border = '3px #c5c3c3ca solid';
            }
            if(color3_btn){
                color3_btn.style.width = '30px';
                color3_btn.style.height = '30px';
                color3_btn.style.border = '3px #c5c3c3ca solid';
            }

            color4_btn.style.width = '35px';
            color4_btn.style.height = '35px';
            color4_btn.style.border = '5px solid black'
            if(color5_btn){
                color5_btn.style.width = '30px';
                color5_btn.style.height = '30px';
                color5_btn.style.border = '3px #c5c3c3ca solid';
            }

            color_take.value = color4_btn.value;
        }
    }
    if(color5_btn){
        color5_btn.onclick = function(){
            if(color1_btn){
                color1_btn.style.width = '30px';
                color1_btn.style.height = '30px';
                color1_btn.style.border = '3px #c5c3c3ca solid';
            }
            if(color2_btn){
                color2_btn.style.width = '30px';
                color2_btn.style.height = '30px';
                color2_btn.style.border = '3px #c5c3c3ca solid';
            }
            if(color3_btn){
                color3_btn.style.width = '30px';
                color3_btn.style.height = '30px';
                color3_btn.style.border = '3px #c5c3c3ca solid';
            }
            if(color4_btn){
                color4_btn.style.width = '30px';
                color4_btn.style.height = '30px';
                color4_btn.style.border = '3px #c5c3c3ca solid';
            }

            color5_btn.style.width = '35px';
            color5_btn.style.height = '35px';
            color5_btn.style.border = '5px solid black'
            color_take.value = color5_btn.value;
        }
    }


}













//show the creator inputs area:
let controll = document.getElementById('controll');
let controll_option = document.getElementById('controll-option');
add_new_product_here_btn_women = document.getElementById('add_new_product_here_btn_women');

let sections_div = document.getElementById('sections_div');
let sections_ul = document.getElementById('sections_ul');
let sections_menu_women_btn = document.getElementById('sections_menu_women_btn');
let sections_submenu_women_ul = document.getElementById('sections_submenu_women_ul');
let sections_submenu_clothing_btn = document.getElementById('sections_submenu_clothing_btn');
let sections_submenu_footwears_btn = document.getElementById('sections_submenu_footwears_btn');
let sections_submenu_bags_btn = document.getElementById('sections_submenu_bags_btn');
let sections_submenu_jewelryandaccessories_btn = document.getElementById('sections_submenu_jewelryandaccessories_btn');
let sections_submenu_beauty_btn = document.getElementById('sections_submenu_beauty_btn');

let sections_subsub_clothing_ul = document.getElementById('sections_subsub_clothing_ul');
let sections_menu_men_btn = document.getElementById('sections_menu_men_btn');
let sections_menu_kids_btn = document.getElementById('sections_menu_kids_btn');
let sections_menu_newarrival_btn = document.getElementById('sections_menu_newarrival_btn');
let sections_menu_bestsellers_btn = document.getElementById('sections_menu_bestsellers_btn');
let sections_menu_brands_btn = document.getElementById('sections_menu_brands_btn');
let sections_menu_sale_btn = document.getElementById('sections_menu_sale_btn');

let sections_subsub_footwears_ul = document.getElementById('sections_subsub_footwears_ul');
let sections_subsub_bags_ul = document.getElementById('sections_subsub_bags_ul');
let sections_subsub_jewelryandaccessories_ul = document.getElementById('sections_subsub_jewelryandaccessories_ul');
let sections_subsub_beauty_ul = document.getElementById('sections_subsub_beauty_ul');

let sections_submenu_men_ul = document.getElementById('sections_submenu_men_ul');
let sections_subsub_clothing_men_ul = document.getElementById('sections_subsub_clothing_men_ul');
let sections_subsub_footwear_men_ul = document.getElementById('sections_subsub_footwear_men_ul');
let sections_subsub_accessories_men_ul = document.getElementById('sections_subsub_accessories_men_ul');
let sections_subsub_beauty_men_ul = document.getElementById('sections_subsub_beauty_men_ul');


let sections_submenu_kids_ul = document.getElementById('sections_submenu_kids_ul');
let sections_subsub_boys_kids_ul = document.getElementById('sections_subsub_boys_kids_ul');
let sections_subsub_girls_kids_ul = document.getElementById('sections_subsub_girls_kids_ul');

let sections_submenu_newarrival_ul = document.getElementById('sections_submenu_newarrival_ul');

let sections_submenu_bestsellers_ul = document.getElementById('sections_submenu_bestsellers_ul');

let sections_submenu_brands_ul = document.getElementById('sections_submenu_brands_ul');

let sections_submenu_sale_ul = document.getElementById('sections_submenu_sale_ul');
let hide_me_now_men = document.getElementById('hide_me_now_men');
let hide_me_now_kids = document.getElementById('hide_me_now_kids');
let hide_me_now_newarrival = document.getElementById('hide_me_now_newarrival');
let hide_me_now_bestsellers = document.getElementById('hide_me_now_bestsellers');
let hide_me_now_brands = document.getElementById('hide_me_now_brands');
let hide_me_now_sale = document.getElementById('hide_me_now_sale');
let media1350px = window.matchMedia("(max-width: 1350px)");

if(owner){
    if(controll_pad){

        function sections(){

            if(media1350px.matches){
                if(sections_div.style.display == "none")
                {
                    sections_div.style.display = "block";
                    // sections_menu_women_btn.style.paddingRight = "568px";
                    sections_menu_women_btn.style.paddingRight = "100%";
                    // sections_menu_men_btn.style.paddingRight = "598px";
                    sections_menu_men_btn.style.paddingRight = "100%";
                    // sections_menu_kids_btn.style.paddingRight = "595px";
                    sections_menu_kids_btn.style.paddingRight = "100%";
                    // sections_menu_newarrival_btn.style.paddingRight = "526px";
                    sections_menu_newarrival_btn.style.paddingRight = "100%";
                    // sections_menu_bestsellers_btn.style.paddingRight = "533px";
                    sections_menu_bestsellers_btn.style.paddingRight = "100%";
                    // sections_menu_brands_btn.style.paddingRight = "569px";
                    sections_menu_brands_btn.style.paddingRight = "100%";
                    // sections_menu_sale_btn.style.paddingRight = "595px";
                    sections_menu_sale_btn.style.paddingRight = "100%";

                }else{
                    sections_div.style.display = "none";
                }
            }
            else if(sections_div.style.display == "none")
            {
                sections_div.style.display = "block";
                sections_menu_women_btn.style.paddingRight = "192px";
                sections_menu_men_btn.style.paddingRight = "220px";
                sections_menu_kids_btn.style.paddingRight = "217px";
                sections_menu_newarrival_btn.style.paddingRight = "160px";
                sections_menu_bestsellers_btn.style.paddingRight = "160px";
                sections_menu_brands_btn.style.paddingRight = "198px";
                sections_menu_sale_btn.style.paddingRight = "217px";

            }else{
                sections_div.style.display = "none";

            }


        }
        sections();

        //women section:
        function women_submenu(){
            if(media1350px.matches){
                if(sections_submenu_women_ul.style.display == "none"){
                    sections_submenu_women_ul.style.display = "block";

                    sections_menu_men_btn.innerHTML = "";
                    sections_menu_men_btn.style.paddingRight = "250px";
                    sections_menu_men_btn.style.boxShadow = "0px 0px 0px #9b5de5";
                    hide_me_now_men.style.display = "inline";

                    sections_menu_kids_btn.innerHTML = "";
                    sections_menu_kids_btn.style.paddingRight = "248px";
                    sections_menu_kids_btn.style.boxShadow =  "0px 0px 0px #9b5de5";
                    hide_me_now_kids.style.display = 'inline';

                    sections_menu_newarrival_btn.innerHTML = "";
                    sections_menu_newarrival_btn.style.paddingRight = "250px";
                    sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";
                    hide_me_now_newarrival.style.display = "inline";

                    sections_menu_bestsellers_btn.innerHTML = "";
                    sections_menu_bestsellers_btn.style.paddingRight = "250px";
                    sections_menu_bestsellers_btn.style.boxShadow = "0px 0px 0px #9b5de5";
                    hide_me_now_bestsellers.style.display = "inline";

                    sections_menu_brands_btn.innerHTML = "";
                    sections_menu_brands_btn.style.paddingRight = "250px";
                    sections_menu_brands_btn.style.boxShadow = "0px 0px 0px #9b5de5";
                    hide_me_now_brands.style.display = "inline";

                    sections_menu_sale_btn.innerHTML = "";
                    sections_menu_sale_btn.style.paddingRight = "250px";
                    sections_menu_sale_btn.style.boxShadow = "0px 0px 0px #9b5de5";
                    hide_me_now_sale.style.display = "inline";

                    // sections_submenu_clothing_btn.style.paddingRight = "551px";
                    sections_submenu_clothing_btn.style.paddingRight = "100%";
                    // sections_submenu_footwears_btn.style.paddingRight = "520px";
                    sections_submenu_footwears_btn.style.paddingRight = "100%";
                    // sections_submenu_bags_btn.style.paddingRight = "578px";
                    sections_submenu_bags_btn.style.paddingRight = "100%";
                    // sections_submenu_jewelryandaccessories_btn.style.paddingRight = "441px";
                    sections_submenu_jewelryandaccessories_btn.style.paddingRight = "100%";
                    // sections_submenu_beauty_btn.style.paddingRight = "563px";
                    sections_submenu_beauty_btn.style.paddingRight = "100%";
                }else{
                    sections_submenu_women_ul.style.display = "none";

                    sections_menu_men_btn.innerHTML = "Men";
                    sections_menu_men_btn.style.paddingRight = "211px";
                    sections_menu_men_btn.style.boxShadow = "0px 5px 5px 0px rgba(1 1 1 /0.65)";

                    sections_menu_kids_btn.innerHTML = "Kids";
                    sections_menu_kids_btn.style.paddingRight = "207px";
                    sections_menu_kids_btn.style.boxShadow = "0px 5px 5px 0px rgba(1 1 1 /0.65)";

                    sections_menu_newarrival_btn.innerHTML = "New.arrivals";
                    sections_menu_newarrival_btn.style.paddingRight = "140px";
                    sections_menu_newarrival_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                    sections_menu_bestsellers_btn.innerHTML = "Best.sellers";
                    sections_menu_bestsellers_btn.style.paddingRight = "144px";
                    sections_menu_bestsellers_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                    sections_menu_brands_btn.innerHTML = "Brands";
                    sections_menu_brands_btn.style.paddingRight = "183px";
                    sections_menu_brands_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                    sections_menu_sale_btn.innerHTML = "Sale";
                    sections_menu_sale_btn.style.paddingRight = "209px";
                    sections_menu_sale_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                    hide_me_now_men.style.display = "none";
                    hide_me_now_kids.style.display = "none";
                    hide_me_now_newarrival.style.display = "none";
                    hide_me_now_bestsellers.style.display = "none";
                    hide_me_now_brands.style.display = "none";
                    hide_me_now_sale.style.display = "none";



                    // sections_menu_men_btn.style.paddingRight = "598px";
                    sections_menu_men_btn.style.paddingRight = "100%";
                    // sections_menu_kids_btn.style.paddingRight = "595px";
                    sections_menu_kids_btn.style.paddingRight = "100%";
                    // sections_menu_newarrival_btn.style.paddingRight = "526px";
                    sections_menu_newarrival_btn.style.paddingRight = "100%";
                    // sections_menu_bestsellers_btn.style.paddingRight = "533px";
                    sections_menu_bestsellers_btn.style.paddingRight = "100%";
                    // sections_menu_brands_btn.style.paddingRight = "569px";
                    sections_menu_brands_btn.style.paddingRight = "100%";
                    // sections_menu_sale_btn.style.paddingRight = "595px";
                    sections_menu_sale_btn.style.paddingRight = "100%";
                }
            }
            else if(sections_submenu_women_ul.style.display == "none"){
                sections_submenu_women_ul.style.display = "block";

                sections_submenu_clothing_btn.style.paddingRight = "179px";
                sections_submenu_footwears_btn.style.paddingRight = "150px";
                sections_submenu_bags_btn.style.paddingRight = "198px";
                sections_submenu_jewelryandaccessories_btn.style.paddingRight = "88px";
                sections_submenu_beauty_btn.style.paddingRight = "187PX";

                sections_menu_men_btn.innerHTML = "";
                sections_menu_men_btn.style.paddingRight = "250px";
                sections_menu_men_btn.style.boxShadow = "0px 0px 0px #9b5de5";
                hide_me_now_men.style.display = "inline";

                sections_menu_kids_btn.innerHTML = "";
                sections_menu_kids_btn.style.paddingRight = "248px";
                sections_menu_kids_btn.style.boxShadow =  "0px 0px 0px #9b5de5";
                hide_me_now_kids.style.display = 'inline';

                sections_menu_newarrival_btn.innerHTML = "";
                sections_menu_newarrival_btn.style.paddingRight = "250px";
                sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";
                hide_me_now_newarrival.style.display = "inline";

                sections_menu_bestsellers_btn.innerHTML = "";
                sections_menu_bestsellers_btn.style.paddingRight = "250px";
                sections_menu_bestsellers_btn.style.boxShadow = "0px 0px 0px #9b5de5";
                hide_me_now_bestsellers.style.display = "inline";

                sections_menu_brands_btn.innerHTML = "";
                sections_menu_brands_btn.style.paddingRight = "250px";
                sections_menu_brands_btn.style.boxShadow = "0px 0px 0px #9b5de5";
                hide_me_now_brands.style.display = "inline";

                sections_menu_sale_btn.innerHTML = "";
                sections_menu_sale_btn.style.paddingRight = "250px";
                sections_menu_sale_btn.style.boxShadow = "0px 0px 0px #9b5de5";
                hide_me_now_sale.style.display = "inline"
            }else{
                sections_submenu_women_ul.style.display = "none";


                sections_menu_men_btn.innerHTML = "Men";
                sections_menu_men_btn.style.paddingRight = "220px";
                sections_menu_men_btn.style.boxShadow = "0px 5px 5px 0px rgba(1 1 1 /0.65)";

                sections_menu_kids_btn.innerHTML = "Kids";
                sections_menu_kids_btn.style.paddingRight = "217px";
                sections_menu_kids_btn.style.boxShadow = "0px 5px 5px 0px rgba(1 1 1 /0.65)";

                sections_menu_newarrival_btn.innerHTML = "New.arrivals";
                sections_menu_newarrival_btn.style.paddingRight = "160px";
                sections_menu_newarrival_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                sections_menu_bestsellers_btn.innerHTML = "Best.sellers";
                sections_menu_bestsellers_btn.style.paddingRight = "160px";
                sections_menu_bestsellers_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                sections_menu_brands_btn.innerHTML = "Brands";
                sections_menu_brands_btn.style.paddingRight = "198px";
                sections_menu_brands_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                sections_menu_sale_btn.innerHTML = "Sale";
                sections_menu_sale_btn.style.paddingRight = "217px";
                sections_menu_sale_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                hide_me_now_men.style.display = "none";
                hide_me_now_kids.style.display = "none";
                hide_me_now_newarrival.style.display = "none";
                hide_me_now_bestsellers.style.display = "none";
                hide_me_now_brands.style.display = "none";
                hide_me_now_sale.style.display = "none";
            }
        }
        women_submenu()
        function clothing_subsub(){
            if(media1350px.matches){
                if(sections_subsub_clothing_ul.style.display == "none"){
                    sections_subsub_clothing_ul.style.display = "block";

                    sections_menu_men_btn.innerHTML = "";
                    sections_menu_men_btn.style.paddingRight = "250px";

                    sections_menu_kids_btn.innerHTML = "";
                    sections_menu_kids_btn.style.paddingRight = "248px";

                    sections_menu_newarrival_btn.innerHTML = "";
                    sections_menu_newarrival_btn.style.paddingRight = "100%";
                    sections_menu_newarrival_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                    sections_menu_bestsellers_btn.innerHTML = "";
                    sections_menu_bestsellers_btn.style.paddingRight = "100%";
                    sections_menu_bestsellers_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                    sections_menu_brands_btn.innerHTML = "";
                    sections_menu_brands_btn.style.paddingRight = "100%";
                    sections_menu_brands_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                    sections_menu_sale_btn.innerHTML = "";
                    sections_menu_sale_btn.style.paddingRight = "100%";
                    sections_menu_sale_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                }else{
                    if(sections_submenu_women_ul.style.display != "none")
                    {
                        sections_subsub_clothing_ul.style.display = "none";

                        sections_menu_men_btn.innerHTML = "";
                        sections_menu_men_btn.style.paddingRight = "250px";
                        sections_menu_men_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                        sections_menu_kids_btn.innerHTML = "";
                        sections_menu_kids_btn.style.paddingRight = "248px";
                        sections_menu_kids_btn.style.boxShadow =  "0px 0px 0px #9b5de5";

                        sections_menu_newarrival_btn.innerHTML = "";
                        sections_menu_newarrival_btn.style.paddingRight = "250px";
                        sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                        sections_menu_bestsellers_btn.innerHTML = "";
                        sections_menu_bestsellers_btn.style.paddingRight = "250px";
                        sections_menu_bestsellers_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                        sections_menu_brands_btn.innerHTML = "";
                        sections_menu_brands_btn.style.paddingRight = "250px";
                        sections_menu_brands_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                        sections_menu_sale_btn.innerHTML = "";
                        sections_menu_sale_btn.style.paddingRight = "250px";
                        sections_menu_sale_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    }else{
                        sections_subsub_clothing_ul.style.display = "none";
                    }

                }
            }
            else if(sections_subsub_clothing_ul.style.display == "none"){
                sections_subsub_clothing_ul.style.display = "block";

                sections_menu_men_btn.innerHTML = "";
                sections_menu_men_btn.style.paddingRight = "250px";

                sections_menu_kids_btn.innerHTML = "";
                sections_menu_kids_btn.style.paddingRight = "248px";

                sections_menu_newarrival_btn.innerHTML = "";
                sections_menu_newarrival_btn.style.paddingRight = "250px";
                sections_menu_newarrival_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                sections_menu_bestsellers_btn.innerHTML = "";
                sections_menu_bestsellers_btn.style.paddingRight = "250px";
                sections_menu_bestsellers_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                sections_menu_brands_btn.innerHTML = "";
                sections_menu_brands_btn.style.paddingRight = "250px";
                sections_menu_brands_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                sections_menu_sale_btn.innerHTML = "";
                sections_menu_sale_btn.style.paddingRight = "250px";
                sections_menu_sale_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

            }else{
                if(sections_submenu_women_ul.style.display != "none")
                {
                    sections_subsub_clothing_ul.style.display = "none";

                    sections_menu_men_btn.innerHTML = "";
                    sections_menu_men_btn.style.paddingRight = "250px";
                    sections_menu_men_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_kids_btn.innerHTML = "";
                    sections_menu_kids_btn.style.paddingRight = "248px";
                    sections_menu_kids_btn.style.boxShadow =  "0px 0px 0px #9b5de5";

                    sections_menu_newarrival_btn.innerHTML = "";
                    sections_menu_newarrival_btn.style.paddingRight = "250px";
                    sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_bestsellers_btn.innerHTML = "";
                    sections_menu_bestsellers_btn.style.paddingRight = "250px";
                    sections_menu_bestsellers_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_brands_btn.innerHTML = "";
                    sections_menu_brands_btn.style.paddingRight = "250px";
                    sections_menu_brands_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_sale_btn.innerHTML = "";
                    sections_menu_sale_btn.style.paddingRight = "250px";
                    sections_menu_sale_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                }else{
                    sections_subsub_clothing_ul.style.display = "none";
                }

            }
        }
        clothing_subsub()
        function footwears_subsub(){
            if(media1350px.matches){
                if(sections_subsub_footwears_ul.style.display == "none"){
                    sections_subsub_footwears_ul.style.display = "block";

                    sections_menu_men_btn.innerHTML = "";
                    sections_menu_men_btn.style.paddingRight = "250px";

                    sections_menu_kids_btn.innerHTML = "";
                    sections_menu_kids_btn.style.paddingRight = "248px";

                    sections_menu_newarrival_btn.innerHTML = "";
                    sections_menu_newarrival_btn.style.paddingRight = "250px";
                    sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_bestsellers_btn.innerHTML = "";
                    sections_menu_bestsellers_btn.style.paddingRight = "100%";
                    sections_menu_bestsellers_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                    sections_menu_brands_btn.innerHTML = "";
                    sections_menu_brands_btn.style.paddingRight = "100%";
                    sections_menu_brands_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                    sections_menu_sale_btn.innerHTML = "";
                    sections_menu_sale_btn.style.paddingRight = "100%";
                    sections_menu_sale_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                }else{

                    if(sections_submenu_women_ul.style.display != "none")
                    {
                        sections_subsub_footwears_ul.style.display = "none";

                        sections_menu_men_btn.innerHTML = "";
                        sections_menu_men_btn.style.paddingRight = "250px";
                        sections_menu_men_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                        sections_menu_kids_btn.innerHTML = "";
                        sections_menu_kids_btn.style.paddingRight = "248px";
                        sections_menu_kids_btn.style.boxShadow =  "0px 0px 0px #9b5de5";

                        sections_menu_newarrival_btn.innerHTML = "";
                        sections_menu_newarrival_btn.style.paddingRight = "250px";
                        sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                        sections_menu_bestsellers_btn.innerHTML = "";
                        sections_menu_bestsellers_btn.style.paddingRight = "250px";
                        sections_menu_bestsellers_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                        sections_menu_brands_btn.innerHTML = "";
                        sections_menu_brands_btn.style.paddingRight = "250px";
                        sections_menu_brands_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                        sections_menu_sale_btn.innerHTML = "";
                        sections_menu_sale_btn.style.paddingRight = "250px";
                        sections_menu_sale_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    }else{
                        sections_subsub_footwears_ul.style.display = "none";
                    }

                }
            }
            else if(sections_subsub_footwears_ul.style.display == "none"){
                sections_subsub_footwears_ul.style.display = "block";

                sections_menu_men_btn.innerHTML = "";
                sections_menu_men_btn.style.paddingRight = "250px";

                sections_menu_kids_btn.innerHTML = "";
                sections_menu_kids_btn.style.paddingRight = "248px";

                sections_menu_newarrival_btn.innerHTML = "";
                sections_menu_newarrival_btn.style.paddingRight = "250px";
                sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                sections_menu_bestsellers_btn.innerHTML = "";
                sections_menu_bestsellers_btn.style.paddingRight = "250px";
                sections_menu_bestsellers_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                sections_menu_brands_btn.innerHTML = "";
                sections_menu_brands_btn.style.paddingRight = "250px";
                sections_menu_brands_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                sections_menu_sale_btn.innerHTML = "";
                sections_menu_sale_btn.style.paddingRight = "250px";
                sections_menu_sale_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

            }else{

                if(sections_submenu_women_ul.style.display != "none")
                {
                    sections_subsub_footwears_ul.style.display = "none";

                    sections_menu_men_btn.innerHTML = "";
                    sections_menu_men_btn.style.paddingRight = "250px";
                    sections_menu_men_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_kids_btn.innerHTML = "";
                    sections_menu_kids_btn.style.paddingRight = "248px";
                    sections_menu_kids_btn.style.boxShadow =  "0px 0px 0px #9b5de5";

                    sections_menu_newarrival_btn.innerHTML = "";
                    sections_menu_newarrival_btn.style.paddingRight = "250px";
                    sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_bestsellers_btn.innerHTML = "";
                    sections_menu_bestsellers_btn.style.paddingRight = "250px";
                    sections_menu_bestsellers_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_brands_btn.innerHTML = "";
                    sections_menu_brands_btn.style.paddingRight = "250px";
                    sections_menu_brands_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_sale_btn.innerHTML = "";
                    sections_menu_sale_btn.style.paddingRight = "250px";
                    sections_menu_sale_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                }else{
                    sections_subsub_footwears_ul.style.display = "none";
                }

            }
        }
        footwears_subsub()
        function bags_subsub(){
            if(media1350px.matches){
                if(sections_subsub_bags_ul.style.display == "none"){
                    sections_subsub_bags_ul.style.display = 'block';

                    sections_menu_men_btn.innerHTML = "";
                    sections_menu_men_btn.style.paddingRight = "250px";

                    sections_menu_kids_btn.innerHTML = "";
                    sections_menu_kids_btn.style.paddingRight = "248px";

                    sections_menu_newarrival_btn.innerHTML = "";
                    sections_menu_newarrival_btn.style.paddingRight = "250px";
                    sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_bestsellers_btn.innerHTML = "";
                    sections_menu_bestsellers_btn.style.paddingRight = "100%";
                    sections_menu_bestsellers_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                    sections_menu_brands_btn.innerHTML = "";
                    sections_menu_brands_btn.style.paddingRight = "100%";
                    sections_menu_brands_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                    sections_menu_sale_btn.innerHTML = "";
                    sections_menu_sale_btn.style.paddingRight = "100%";
                    sections_menu_sale_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                }else{

                    if(sections_submenu_women_ul.style.display != "none")
                    {
                        sections_subsub_bags_ul.style.display = "none";

                        sections_menu_men_btn.innerHTML = "";
                        sections_menu_men_btn.style.paddingRight = "250px";
                        sections_menu_men_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                        sections_menu_kids_btn.innerHTML = "";
                        sections_menu_kids_btn.style.paddingRight = "248px";
                        sections_menu_kids_btn.style.boxShadow =  "0px 0px 0px #9b5de5";

                        sections_menu_newarrival_btn.innerHTML = "";
                        sections_menu_newarrival_btn.style.paddingRight = "250px";
                        sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                        sections_menu_bestsellers_btn.innerHTML = "";
                        sections_menu_bestsellers_btn.style.paddingRight = "250";
                        sections_menu_bestsellers_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                        sections_menu_brands_btn.innerHTML = "";
                        sections_menu_brands_btn.style.paddingRight = "250px";
                        sections_menu_brands_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                        sections_menu_sale_btn.innerHTML = "";
                        sections_menu_sale_btn.style.paddingRight = "250px";
                        sections_menu_sale_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    }else{
                        sections_subsub_bags_ul.style.display = "none";
                    }

                }
            }
            else if(sections_subsub_bags_ul.style.display == "none"){
                sections_subsub_bags_ul.style.display = 'block';

                sections_menu_men_btn.innerHTML = "";
                sections_menu_men_btn.style.paddingRight = "250px";

                sections_menu_kids_btn.innerHTML = "";
                sections_menu_kids_btn.style.paddingRight = "248px";

                sections_menu_newarrival_btn.innerHTML = "";
                sections_menu_newarrival_btn.style.paddingRight = "250px";
                sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                sections_menu_bestsellers_btn.innerHTML = "";
                sections_menu_bestsellers_btn.style.paddingRight = "250px";
                sections_menu_bestsellers_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                sections_menu_brands_btn.innerHTML = "";
                sections_menu_brands_btn.style.paddingRight = "250px";
                sections_menu_brands_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                sections_menu_sale_btn.innerHTML = "";
                sections_menu_sale_btn.style.paddingRight = "250px";
                sections_menu_sale_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

            }else{

                if(sections_submenu_women_ul.style.display != "none")
                {
                    sections_subsub_bags_ul.style.display = "none";

                    sections_menu_men_btn.innerHTML = "";
                    sections_menu_men_btn.style.paddingRight = "250px";
                    sections_menu_men_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_kids_btn.innerHTML = "";
                    sections_menu_kids_btn.style.paddingRight = "248px";
                    sections_menu_kids_btn.style.boxShadow =  "0px 0px 0px #9b5de5";

                    sections_menu_newarrival_btn.innerHTML = "";
                    sections_menu_newarrival_btn.style.paddingRight = "250px";
                    sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_bestsellers_btn.innerHTML = "";
                    sections_menu_bestsellers_btn.style.paddingRight = "250";
                    sections_menu_bestsellers_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_brands_btn.innerHTML = "";
                    sections_menu_brands_btn.style.paddingRight = "250px";
                    sections_menu_brands_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_sale_btn.innerHTML = "";
                    sections_menu_sale_btn.style.paddingRight = "250px";
                    sections_menu_sale_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                }else{
                    sections_subsub_bags_ul.style.display = "none";
                }

            }
        }



        bags_subsub()
        function jewelry_subsub(){
            if(media1350px.matches){
                if(sections_subsub_jewelryandaccessories_ul.style.display == "none"){
                    sections_subsub_jewelryandaccessories_ul.style.display = "block";

                    sections_menu_men_btn.innerHTML = "";
                    sections_menu_men_btn.style.paddingRight = "250px";

                    sections_menu_kids_btn.innerHTML = "";
                    sections_menu_kids_btn.style.paddingRight = "248px";

                    sections_menu_newarrival_btn.innerHTML = "";
                    sections_menu_newarrival_btn.style.paddingRight = "250px";
                    sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_bestsellers_btn.innerHTML = "";
                    sections_menu_bestsellers_btn.style.paddingRight = "100%";
                    sections_menu_bestsellers_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                    sections_menu_brands_btn.innerHTML = "";
                    sections_menu_brands_btn.style.paddingRight = "100%";
                    sections_menu_brands_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                    sections_menu_sale_btn.innerHTML = "";
                    sections_menu_sale_btn.style.paddingRight = "100%";
                    sections_menu_sale_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                }else{

                    if(sections_submenu_women_ul.style.display != "none")
                    {
                        sections_subsub_jewelryandaccessories_ul.style.display = "none";

                        sections_menu_men_btn.innerHTML = "";
                        sections_menu_men_btn.style.paddingRight = "250px";
                        sections_menu_men_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                        sections_menu_kids_btn.innerHTML = "";
                        sections_menu_kids_btn.style.paddingRight = "248px";
                        sections_menu_kids_btn.style.boxShadow =  "0px 0px 0px #9b5de5";

                        sections_menu_newarrival_btn.innerHTML = "";
                        sections_menu_newarrival_btn.style.paddingRight = "250px";
                        sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                        sections_menu_bestsellers_btn.innerHTML = "";
                        sections_menu_bestsellers_btn.style.paddingRight = "250px";
                        sections_menu_bestsellers_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                        sections_menu_brands_btn.innerHTML = "";
                        sections_menu_brands_btn.style.paddingRight = "250px";
                        sections_menu_brands_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                        sections_menu_sale_btn.innerHTML = "";
                        sections_menu_sale_btn.style.paddingRight = "250px";
                        sections_menu_sale_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    }else{
                        sections_subsub_jewelryandaccessories_ul.style.display = "none";
                    }
                }
            }
            else if(sections_subsub_jewelryandaccessories_ul.style.display == "none"){
                sections_subsub_jewelryandaccessories_ul.style.display = "block";

                sections_menu_men_btn.innerHTML = "";
                sections_menu_men_btn.style.paddingRight = "250px";

                sections_menu_kids_btn.innerHTML = "";
                sections_menu_kids_btn.style.paddingRight = "248px";

                sections_menu_newarrival_btn.innerHTML = "";
                sections_menu_newarrival_btn.style.paddingRight = "250px";
                sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                sections_menu_bestsellers_btn.innerHTML = "";
                sections_menu_bestsellers_btn.style.paddingRight = "250px";
                sections_menu_bestsellers_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                sections_menu_brands_btn.innerHTML = "";
                sections_menu_brands_btn.style.paddingRight = "250px";
                sections_menu_brands_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                sections_menu_sale_btn.innerHTML = "";
                sections_menu_sale_btn.style.paddingRight = "250px";
                sections_menu_sale_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

            }else{

                if(sections_submenu_women_ul.style.display != "none")
                {
                    sections_subsub_jewelryandaccessories_ul.style.display = "none";

                    sections_menu_men_btn.innerHTML = "";
                    sections_menu_men_btn.style.paddingRight = "250px";
                    sections_menu_men_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_kids_btn.innerHTML = "";
                    sections_menu_kids_btn.style.paddingRight = "248px";
                    sections_menu_kids_btn.style.boxShadow =  "0px 0px 0px #9b5de5";

                    sections_menu_newarrival_btn.innerHTML = "";
                    sections_menu_newarrival_btn.style.paddingRight = "250px";
                    sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_bestsellers_btn.innerHTML = "";
                    sections_menu_bestsellers_btn.style.paddingRight = "250px";
                    sections_menu_bestsellers_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_brands_btn.innerHTML = "";
                    sections_menu_brands_btn.style.paddingRight = "250px";
                    sections_menu_brands_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_sale_btn.innerHTML = "";
                    sections_menu_sale_btn.style.paddingRight = "250px";
                    sections_menu_sale_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                }else{
                    sections_subsub_jewelryandaccessories_ul.style.display = "none";
                }
            }
        }
        jewelry_subsub()
        function beauty_subsub(){
            if(media1350px.matches){
                if(sections_subsub_beauty_ul.style.display == "none"){
                    sections_subsub_beauty_ul.style.display = "block";

                    sections_menu_men_btn.innerHTML = "";
                    sections_menu_men_btn.style.paddingRight = "250px";

                    sections_menu_kids_btn.innerHTML = "";
                    sections_menu_kids_btn.style.paddingRight = "248px";

                    sections_menu_newarrival_btn.innerHTML = "";
                    sections_menu_newarrival_btn.style.paddingRight = "250px";
                    sections_menu_newarrival_btn.style.boxShadow = " 0px 0px 0px #9b5de5";

                    sections_menu_bestsellers_btn.innerHTML = "";
                    sections_menu_bestsellers_btn.style.paddingRight = "100%";
                    sections_menu_bestsellers_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                    sections_menu_brands_btn.innerHTML = "";
                    sections_menu_brands_btn.style.paddingRight = "100%";
                    sections_menu_brands_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                    sections_menu_sale_btn.innerHTML = "";
                    sections_menu_sale_btn.style.paddingRight = "100%";
                    sections_menu_sale_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                }else{

                    if(sections_submenu_women_ul.style.display != "none")
                    {
                        sections_subsub_beauty_ul.style.display = "none";

                        sections_menu_men_btn.innerHTML = "";
                        sections_menu_men_btn.style.paddingRight = "250px";
                        sections_menu_men_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                        sections_menu_kids_btn.innerHTML = "";
                        sections_menu_kids_btn.style.paddingRight = "248px";
                        sections_menu_kids_btn.style.boxShadow =  "0px 0px 0px #9b5de5";

                        sections_menu_newarrival_btn.innerHTML = "";
                        sections_menu_newarrival_btn.style.paddingRight = "250px";
                        sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                        sections_menu_bestsellers_btn.innerHTML = "";
                        sections_menu_bestsellers_btn.style.paddingRight = "250px";
                        sections_menu_bestsellers_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                        sections_menu_brands_btn.innerHTML = "";
                        sections_menu_brands_btn.style.paddingRight = "250px";
                        sections_menu_brands_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                        sections_menu_sale_btn.innerHTML = "";
                        sections_menu_sale_btn.style.paddingRight = "250px";
                        sections_menu_sale_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    }else{
                        sections_subsub_beauty_ul.style.display = "none";

                    }
                }
            }
            else if(sections_subsub_beauty_ul.style.display == "none"){
                sections_subsub_beauty_ul.style.display = "block";

                sections_menu_men_btn.innerHTML = "";
                sections_menu_men_btn.style.paddingRight = "250px";

                sections_menu_kids_btn.innerHTML = "";
                sections_menu_kids_btn.style.paddingRight = "248px";

                sections_menu_newarrival_btn.innerHTML = "";
                sections_menu_newarrival_btn.style.paddingRight = "250px";
                sections_menu_newarrival_btn.style.boxShadow = " 0px 0px 0px #9b5de5";

                sections_menu_bestsellers_btn.innerHTML = "";
                sections_menu_bestsellers_btn.style.paddingRight = "250px";
                sections_menu_bestsellers_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                sections_menu_brands_btn.innerHTML = "";
                sections_menu_brands_btn.style.paddingRight = "250px";
                sections_menu_brands_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                sections_menu_sale_btn.innerHTML = "";
                sections_menu_sale_btn.style.paddingRight = "250px";
                sections_menu_sale_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

            }else{

                if(sections_submenu_women_ul.style.display != "none")
                {
                    sections_subsub_beauty_ul.style.display = "none";

                    sections_menu_men_btn.innerHTML = "";
                    sections_menu_men_btn.style.paddingRight = "250px";
                    sections_menu_men_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_kids_btn.innerHTML = "";
                    sections_menu_kids_btn.style.paddingRight = "248px";
                    sections_menu_kids_btn.style.boxShadow =  "0px 0px 0px #9b5de5";

                    sections_menu_newarrival_btn.innerHTML = "";
                    sections_menu_newarrival_btn.style.paddingRight = "250px";
                    sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_bestsellers_btn.innerHTML = "";
                    sections_menu_bestsellers_btn.style.paddingRight = "250px";
                    sections_menu_bestsellers_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_brands_btn.innerHTML = "";
                    sections_menu_brands_btn.style.paddingRight = "250px";
                    sections_menu_brands_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_sale_btn.innerHTML = "";
                    sections_menu_sale_btn.style.paddingRight = "250px";
                    sections_menu_sale_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                }else{
                    sections_subsub_beauty_ul.style.display = "none";

                }
            }
        }
        beauty_subsub()

        //men section:
        function men_submenu(){
            if(media1350px.matches){
                if(sections_submenu_men_ul.style.display == "none"){
                    sections_submenu_men_ul.style.display = "block";


                    sections_menu_women_btn.style.boxShadow =  "0px 0px 0px #9b5de5";
                    sections_menu_women_btn.style.display = "none";

                    sections_ul.style.display = "block";

                    sections_menu_kids_btn.innerHTML = "";
                    sections_menu_kids_btn.style.paddingRight = "248px";
                    sections_menu_kids_btn.style.boxShadow =  "0px 0px 0px #9b5de5";

                    sections_menu_newarrival_btn.innerHTML = "";
                    sections_menu_newarrival_btn.style.paddingRight = "250px";
                    sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_bestsellers_btn.innerHTML = "";
                    sections_menu_bestsellers_btn.style.paddingRight = "250px";
                    sections_menu_bestsellers_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_brands_btn.innerHTML = "";
                    sections_menu_brands_btn.style.paddingRight = "250px";
                    sections_menu_brands_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_sale_btn.innerHTML = "";
                    sections_menu_sale_btn.style.paddingRight = "250px";
                    sections_menu_sale_btn.style.boxShadow = "0px 0px 0px #9b5de5";


                    hide_me_now_kids.style.display = "inline";
                    hide_me_now_newarrival.style.display = "inline";
                    hide_me_now_bestsellers.style.display = "inline";
                    hide_me_now_brands.style.display = "inline";
                    hide_me_now_sale.style.display = "inline";




                    // sections_submenu_clothing_men_btn.style.paddingRight = "551px";
                    sections_submenu_clothing_men_btn.style.paddingRight = "100%";
                    // sections_submenu_footwear_men_btn.style.paddingRight = "545px";
                    sections_submenu_footwear_men_btn.style.paddingRight = "100%";
                    // sections_submenu_accessories_men_btn.style.paddingRight = "521px";
                    sections_submenu_accessories_men_btn.style.paddingRight = "100%";
                    // sections_submenu_beauty_men_btn.style.paddingRight = "561px";
                    sections_submenu_beauty_men_btn.style.paddingRight = "100%";

                }else{
                    sections_submenu_men_ul.style.display = "none";

                    sections_menu_women_btn.style.display = "inline";
                    sections_menu_women_btn.style.boxShadow = "0px 5px 5px 0px rgba(1 1 1 /0.65)";

                    sections_ul.style.display = "flex";

                    sections_menu_kids_btn.innerHTML = "Kids";
                    sections_menu_kids_btn.style.paddingRight = "207px";
                    sections_menu_kids_btn.style.boxShadow = "0px 5px 5px 0px rgba(1 1 1 /0.65)";

                    sections_menu_newarrival_btn.innerHTML = "New.arrivals";
                    sections_menu_newarrival_btn.style.paddingRight = "140px";
                    sections_menu_newarrival_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                    sections_menu_bestsellers_btn.innerHTML = "Best.sellers";
                    sections_menu_bestsellers_btn.style.paddingRight = "144px";
                    sections_menu_bestsellers_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                    sections_menu_brands_btn.innerHTML = "Brands";
                    sections_menu_brands_btn.style.paddingRight = "183px";
                    sections_menu_brands_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                    sections_menu_sale_btn.innerHTML = "Sale";
                    sections_menu_sale_btn.style.paddingRight = "209px";
                    sections_menu_sale_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";


                    hide_me_now_kids.style.display = "none";
                    hide_me_now_newarrival.style.display = "none";
                    hide_me_now_bestsellers.style.display = "none";
                    hide_me_now_brands.style.display = "none";
                    hide_me_now_sale.style.display = "none";

                    // sections_menu_kids_btn.style.paddingRight = "595px";
                    sections_menu_kids_btn.style.paddingRight = "100%";
                    // sections_menu_newarrival_btn.style.paddingRight = "526px";
                    sections_menu_newarrival_btn.style.paddingRight = "100%";
                    // sections_menu_bestsellers_btn.style.paddingRight = "533px";
                    sections_menu_bestsellers_btn.style.paddingRight = "100%";
                    // sections_menu_brands_btn.style.paddingRight = "569px";
                    sections_menu_brands_btn.style.paddingRight = "100%";
                    // sections_menu_sale_btn.style.paddingRight = "595px";
                    sections_menu_sale_btn.style.paddingRight = "100%";

                }
            }
            else if(sections_submenu_men_ul.style.display == "none"){
                sections_submenu_men_ul.style.display = "block";

                sections_submenu_clothing_men_btn.style.paddingRight = "179px";
                sections_submenu_footwear_men_btn.style.paddingRight = "172px";
                sections_submenu_accessories_men_btn.style.paddingRight = "150px";
                sections_submenu_beauty_men_btn.style.paddingRight = "187px";


                sections_menu_women_btn.style.boxShadow =  "0px 0px 0px #9b5de5";
                sections_menu_women_btn.style.display = "none";

                sections_ul.style.display = "block";

                sections_menu_kids_btn.innerHTML = "";
                sections_menu_kids_btn.style.paddingRight = "248px";
                sections_menu_kids_btn.style.boxShadow =  "0px 0px 0px #9b5de5";

                sections_menu_newarrival_btn.innerHTML = "";
                sections_menu_newarrival_btn.style.paddingRight = "250px";
                sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                sections_menu_bestsellers_btn.innerHTML = "";
                sections_menu_bestsellers_btn.style.paddingRight = "250px";
                sections_menu_bestsellers_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                sections_menu_brands_btn.innerHTML = "";
                sections_menu_brands_btn.style.paddingRight = "250px";
                sections_menu_brands_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                sections_menu_sale_btn.innerHTML = "";
                sections_menu_sale_btn.style.paddingRight = "250px";
                sections_menu_sale_btn.style.boxShadow = "0px 0px 0px #9b5de5";


                hide_me_now_kids.style.display = "inline";
                hide_me_now_newarrival.style.display = "inline";
                hide_me_now_bestsellers.style.display = "inline";
                hide_me_now_brands.style.display = "inline";
                hide_me_now_sale.style.display = "inline";

            }else{
                sections_submenu_men_ul.style.display = "none";


                sections_menu_women_btn.style.display = "inline";
                sections_menu_women_btn.style.boxShadow = "0px 5px 5px 0px rgba(1 1 1 /0.65)";

                sections_ul.style.display = "flex";

                sections_menu_kids_btn.innerHTML = "Kids";
                sections_menu_kids_btn.style.paddingRight = "217px";
                sections_menu_kids_btn.style.boxShadow = "0px 5px 5px 0px rgba(1 1 1 /0.65)";

                sections_menu_newarrival_btn.innerHTML = "New.arrivals";
                sections_menu_newarrival_btn.style.paddingRight = "160px";
                sections_menu_newarrival_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                sections_menu_bestsellers_btn.innerHTML = "Best.sellers";
                sections_menu_bestsellers_btn.style.paddingRight = "160px";
                sections_menu_bestsellers_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                sections_menu_brands_btn.innerHTML = "Brands";
                sections_menu_brands_btn.style.paddingRight = "198px";
                sections_menu_brands_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                sections_menu_sale_btn.innerHTML = "Sale";
                sections_menu_sale_btn.style.paddingRight = "217px";
                sections_menu_sale_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";


                hide_me_now_kids.style.display = "none";
                hide_me_now_newarrival.style.display = "none";
                hide_me_now_bestsellers.style.display = "none";
                hide_me_now_brands.style.display = "none";
                hide_me_now_sale.style.display = "none";

            }
        }
        men_submenu()
        function men_clothing_subsub(){
            if(media1350px.matches){
                if(sections_subsub_clothing_men_ul.style.display == "none"){
                    sections_subsub_clothing_men_ul.style.display = "block";

                    sections_menu_kids_btn.innerHTML = "";
                    sections_menu_kids_btn.style.paddingRight = "248px";

                    sections_menu_newarrival_btn.innerHTML = "";
                    sections_menu_newarrival_btn.style.paddingRight = "250px";
                    sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_bestsellers_btn.innerHTML = "";
                    sections_menu_bestsellers_btn.style.paddingRight = "100%";
                    sections_menu_bestsellers_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                    sections_menu_brands_btn.innerHTML = "";
                    sections_menu_brands_btn.style.paddingRight = "100%";
                    sections_menu_brands_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                    sections_menu_sale_btn.innerHTML = "";
                    sections_menu_sale_btn.style.paddingRight = "100%";
                    sections_menu_sale_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                }else{

                    if(sections_submenu_men_ul.style.display != "none")
                    {
                        sections_subsub_clothing_men_ul.style.display = "none";

                        sections_menu_kids_btn.innerHTML = "";
                        sections_menu_kids_btn.style.paddingRight = "248px";
                        sections_menu_kids_btn.style.boxShadow =  "0px 0px 0px #9b5de5";

                        sections_menu_newarrival_btn.innerHTML = "";
                        sections_menu_newarrival_btn.style.paddingRight = "250px";
                        sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                        sections_menu_bestsellers_btn.innerHTML = "";
                        sections_menu_bestsellers_btn.style.paddingRight = "250px";
                        sections_menu_bestsellers_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                        sections_menu_brands_btn.innerHTML = "";
                        sections_menu_brands_btn.style.paddingRight = "250px";
                        sections_menu_brands_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                        sections_menu_sale_btn.innerHTML = "";
                        sections_menu_sale_btn.style.paddingRight = "250px";
                        sections_menu_sale_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    }else{
                        sections_subsub_clothing_men_ul.style.display = "none";
                    }
                }
            }
            else if(sections_subsub_clothing_men_ul.style.display == "none"){
                sections_subsub_clothing_men_ul.style.display = "block";

                sections_menu_kids_btn.innerHTML = "";
                sections_menu_kids_btn.style.paddingRight = "248px";

                sections_menu_newarrival_btn.innerHTML = "";
                sections_menu_newarrival_btn.style.paddingRight = "250px";
                sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                sections_menu_bestsellers_btn.innerHTML = "";
                sections_menu_bestsellers_btn.style.paddingRight = "250px";
                sections_menu_bestsellers_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                sections_menu_brands_btn.innerHTML = "";
                sections_menu_brands_btn.style.paddingRight = "250px";
                sections_menu_brands_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                sections_menu_sale_btn.innerHTML = "";
                sections_menu_sale_btn.style.paddingRight = "250px";
                sections_menu_sale_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

            }else{

                if(sections_submenu_men_ul.style.display != "none")
                {
                    sections_subsub_clothing_men_ul.style.display = "none";

                    sections_menu_kids_btn.innerHTML = "";
                    sections_menu_kids_btn.style.paddingRight = "248px";
                    sections_menu_kids_btn.style.boxShadow =  "0px 0px 0px #9b5de5";

                    sections_menu_newarrival_btn.innerHTML = "";
                    sections_menu_newarrival_btn.style.paddingRight = "250px";
                    sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_bestsellers_btn.innerHTML = "";
                    sections_menu_bestsellers_btn.style.paddingRight = "250px";
                    sections_menu_bestsellers_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_brands_btn.innerHTML = "";
                    sections_menu_brands_btn.style.paddingRight = "250px";
                    sections_menu_brands_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_sale_btn.innerHTML = "";
                    sections_menu_sale_btn.style.paddingRight = "250px";
                    sections_menu_sale_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                }else{
                    sections_subsub_clothing_men_ul.style.display = "none";
                }
            }
        }
        men_clothing_subsub()
        function men_footwear_subsub(){
            if(media1350px.matches){
                if(sections_subsub_footwear_men_ul.style.display == "none"){
                    sections_subsub_footwear_men_ul.style.display = "block";

                    sections_menu_kids_btn.innerHTML = "";
                    sections_menu_kids_btn.style.paddingRight = "248px";

                    sections_menu_newarrival_btn.innerHTML = "";
                    sections_menu_newarrival_btn.style.paddingRight = "250px";
                    sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_bestsellers_btn.innerHTML = "";
                    sections_menu_bestsellers_btn.style.paddingRight = "100%";
                    sections_menu_bestsellers_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                    sections_menu_brands_btn.innerHTML = "";
                    sections_menu_brands_btn.style.paddingRight = "100%";
                    sections_menu_brands_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                    sections_menu_sale_btn.innerHTML = "";
                    sections_menu_sale_btn.style.paddingRight = "100%";
                    sections_menu_sale_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                }else{

                    if(sections_submenu_men_ul.style.display != "none")
                    {
                        sections_subsub_footwear_men_ul.style.display = "none";

                        sections_menu_kids_btn.innerHTML = "";
                        sections_menu_kids_btn.style.paddingRight = "248px";
                        sections_menu_kids_btn.style.boxShadow =  "0px 0px 0px #9b5de5";

                        sections_menu_newarrival_btn.innerHTML = "";
                        sections_menu_newarrival_btn.style.paddingRight = "250px";
                        sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                        sections_menu_bestsellers_btn.innerHTML = "";
                        sections_menu_bestsellers_btn.style.paddingRight = "250px";
                        sections_menu_bestsellers_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                        sections_menu_brands_btn.innerHTML = "";
                        sections_menu_brands_btn.style.paddingRight = "250px";
                        sections_menu_brands_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                        sections_menu_sale_btn.innerHTML = "";
                        sections_menu_sale_btn.style.paddingRight = "250px";
                        sections_menu_sale_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    }else{
                        sections_subsub_footwear_men_ul.style.display = "none";
                    }
                }
            }
            else if(sections_subsub_footwear_men_ul.style.display == "none"){
                sections_subsub_footwear_men_ul.style.display = "block";

                sections_menu_kids_btn.innerHTML = "";
                sections_menu_kids_btn.style.paddingRight = "248px";

                sections_menu_newarrival_btn.innerHTML = "";
                sections_menu_newarrival_btn.style.paddingRight = "250px";
                sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                sections_menu_bestsellers_btn.innerHTML = "";
                sections_menu_bestsellers_btn.style.paddingRight = "250px";
                sections_menu_bestsellers_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                sections_menu_brands_btn.innerHTML = "";
                sections_menu_brands_btn.style.paddingRight = "250px";
                sections_menu_brands_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                sections_menu_sale_btn.innerHTML = "";
                sections_menu_sale_btn.style.paddingRight = "250px";
                sections_menu_sale_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

            }else{

                if(sections_submenu_men_ul.style.display != "none")
                {
                    sections_subsub_footwear_men_ul.style.display = "none";

                    sections_menu_kids_btn.innerHTML = "";
                    sections_menu_kids_btn.style.paddingRight = "248px";
                    sections_menu_kids_btn.style.boxShadow =  "0px 0px 0px #9b5de5";

                    sections_menu_newarrival_btn.innerHTML = "";
                    sections_menu_newarrival_btn.style.paddingRight = "250px";
                    sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_bestsellers_btn.innerHTML = "";
                    sections_menu_bestsellers_btn.style.paddingRight = "250px";
                    sections_menu_bestsellers_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_brands_btn.innerHTML = "";
                    sections_menu_brands_btn.style.paddingRight = "250px";
                    sections_menu_brands_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_sale_btn.innerHTML = "";
                    sections_menu_sale_btn.style.paddingRight = "250px";
                    sections_menu_sale_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                }else{
                    sections_subsub_footwear_men_ul.style.display = "none";
                }
            }
        }

        men_footwear_subsub()
        function men_accessories_subsub(){
            if(media1350px.matches){
                if(sections_subsub_accessories_men_ul.style.display == "none"){
                    sections_subsub_accessories_men_ul.style.display = "block";

                    sections_menu_kids_btn.innerHTML = "";
                    sections_menu_kids_btn.style.paddingRight = "248px";

                    sections_menu_newarrival_btn.innerHTML = "";
                    sections_menu_newarrival_btn.style.paddingRight = "250px";
                    sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_bestsellers_btn.innerHTML = "";
                    sections_menu_bestsellers_btn.style.paddingRight = "100%";
                    sections_menu_bestsellers_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                    sections_menu_brands_btn.innerHTML = "";
                    sections_menu_brands_btn.style.paddingRight = "100%";
                    sections_menu_brands_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                    sections_menu_sale_btn.innerHTML = "";
                    sections_menu_sale_btn.style.paddingRight = "100%";
                    sections_menu_sale_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                }else{

                    if(sections_submenu_men_ul.style.display != "none")
                    {
                        sections_subsub_accessories_men_ul.style.display = "none";

                        sections_menu_kids_btn.innerHTML = "";
                        sections_menu_kids_btn.style.paddingRight = "248px";
                        sections_menu_kids_btn.style.boxShadow =  "0px 0px 0px #9b5de5";

                        sections_menu_newarrival_btn.innerHTML = "";
                        sections_menu_newarrival_btn.style.paddingRight = "250px";
                        sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                        sections_menu_bestsellers_btn.innerHTML = "";
                        sections_menu_bestsellers_btn.style.paddingRight = "250px";
                        sections_menu_bestsellers_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                        sections_menu_brands_btn.innerHTML = "";
                        sections_menu_brands_btn.style.paddingRight = "250px";
                        sections_menu_brands_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                        sections_menu_sale_btn.innerHTML = "";
                        sections_menu_sale_btn.style.paddingRight = "250px";
                        sections_menu_sale_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    }else{
                        sections_subsub_accessories_men_ul.style.display = "none";
                    }
                }
            }
            else if(sections_subsub_accessories_men_ul.style.display == "none"){
                sections_subsub_accessories_men_ul.style.display = "block";

                sections_menu_kids_btn.innerHTML = "";
                sections_menu_kids_btn.style.paddingRight = "248px";

                sections_menu_newarrival_btn.innerHTML = "";
                sections_menu_newarrival_btn.style.paddingRight = "250px";
                sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                sections_menu_bestsellers_btn.innerHTML = "";
                sections_menu_bestsellers_btn.style.paddingRight = "250px";
                sections_menu_bestsellers_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                sections_menu_brands_btn.innerHTML = "";
                sections_menu_brands_btn.style.paddingRight = "250px";
                sections_menu_brands_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                sections_menu_sale_btn.innerHTML = "";
                sections_menu_sale_btn.style.paddingRight = "250px";
                sections_menu_sale_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

            }else{

                if(sections_submenu_men_ul.style.display != "none")
                {
                    sections_subsub_accessories_men_ul.style.display = "none";

                    sections_menu_kids_btn.innerHTML = "";
                    sections_menu_kids_btn.style.paddingRight = "248px";
                    sections_menu_kids_btn.style.boxShadow =  "0px 0px 0px #9b5de5";

                    sections_menu_newarrival_btn.innerHTML = "";
                    sections_menu_newarrival_btn.style.paddingRight = "250px";
                    sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_bestsellers_btn.innerHTML = "";
                    sections_menu_bestsellers_btn.style.paddingRight = "250px";
                    sections_menu_bestsellers_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_brands_btn.innerHTML = "";
                    sections_menu_brands_btn.style.paddingRight = "250px";
                    sections_menu_brands_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_sale_btn.innerHTML = "";
                    sections_menu_sale_btn.style.paddingRight = "250px";
                    sections_menu_sale_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                }else{
                    sections_subsub_accessories_men_ul.style.display = "none";
                }
            }
        }
        men_accessories_subsub()
        function men_beauty_subsub(){
            if(media1350px.matches){
                if(sections_subsub_beauty_men_ul.style.display == "none"){
                    sections_subsub_beauty_men_ul.style.display = "block";

                    sections_menu_kids_btn.innerHTML = "";
                    sections_menu_kids_btn.style.paddingRight = "248px";

                    sections_menu_newarrival_btn.innerHTML = "";
                    sections_menu_newarrival_btn.style.paddingRight = "250px";
                    sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_bestsellers_btn.innerHTML = "";
                    sections_menu_bestsellers_btn.style.paddingRight = "100%";
                    sections_menu_bestsellers_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                    sections_menu_brands_btn.innerHTML = "";
                    sections_menu_brands_btn.style.paddingRight = "100%";
                    sections_menu_brands_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                    sections_menu_sale_btn.innerHTML = "";
                    sections_menu_sale_btn.style.paddingRight = "100%";
                    sections_menu_sale_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                }else{

                    if(sections_submenu_men_ul.style.display != "none")
                    {
                        sections_subsub_beauty_men_ul.style.display = "none";

                        sections_menu_kids_btn.innerHTML = "";
                        sections_menu_kids_btn.style.paddingRight = "248px";
                        sections_menu_kids_btn.style.boxShadow =  "0px 0px 0px #9b5de5";

                        sections_menu_newarrival_btn.innerHTML = "";
                        sections_menu_newarrival_btn.style.paddingRight = "250px";
                        sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                        sections_menu_bestsellers_btn.innerHTML = "";
                        sections_menu_bestsellers_btn.style.paddingRight = "250px";
                        sections_menu_bestsellers_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                        sections_menu_brands_btn.innerHTML = "";
                        sections_menu_brands_btn.style.paddingRight = "250px";
                        sections_menu_brands_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                        sections_menu_sale_btn.innerHTML = "";
                        sections_menu_sale_btn.style.paddingRight = "250px";
                        sections_menu_sale_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    }else{
                        sections_subsub_beauty_men_ul.style.display = "none";
                    }
                }
            }
            else if(sections_subsub_beauty_men_ul.style.display == "none"){
                sections_subsub_beauty_men_ul.style.display = "block";

                sections_menu_kids_btn.innerHTML = "";
                sections_menu_kids_btn.style.paddingRight = "248px";

                sections_menu_newarrival_btn.innerHTML = "";
                sections_menu_newarrival_btn.style.paddingRight = "250px";
                sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                sections_menu_bestsellers_btn.innerHTML = "";
                sections_menu_bestsellers_btn.style.paddingRight = "250px";
                sections_menu_bestsellers_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                sections_menu_brands_btn.innerHTML = "";
                sections_menu_brands_btn.style.paddingRight = "250px";
                sections_menu_brands_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                sections_menu_sale_btn.innerHTML = "";
                sections_menu_sale_btn.style.paddingRight = "250px";
                sections_menu_sale_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

            }else{

                if(sections_submenu_men_ul.style.display != "none")
                {
                    sections_subsub_beauty_men_ul.style.display = "none";

                    sections_menu_kids_btn.innerHTML = "";
                    sections_menu_kids_btn.style.paddingRight = "248px";
                    sections_menu_kids_btn.style.boxShadow =  "0px 0px 0px #9b5de5";

                    sections_menu_newarrival_btn.innerHTML = "";
                    sections_menu_newarrival_btn.style.paddingRight = "250px";
                    sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_bestsellers_btn.innerHTML = "";
                    sections_menu_bestsellers_btn.style.paddingRight = "250px";
                    sections_menu_bestsellers_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_brands_btn.innerHTML = "";
                    sections_menu_brands_btn.style.paddingRight = "250px";
                    sections_menu_brands_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_sale_btn.innerHTML = "";
                    sections_menu_sale_btn.style.paddingRight = "250px";
                    sections_menu_sale_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                }else{
                    sections_subsub_beauty_men_ul.style.display = "none";
                }
            }
        }
        men_beauty_subsub()



        //kids section:
        function kids_submenu(){
            if(media1350px.matches){
                if(sections_submenu_kids_ul.style.display == "none"){
                    sections_submenu_kids_ul.style.display = "block";

                    sections_menu_women_btn.style.display = "none";
                    sections_menu_men_btn.style.display = "none";

                    sections_ul.style.display = "block";

                    sections_menu_newarrival_btn.innerHTML = "";
                    sections_menu_newarrival_btn.style.paddingRight = "250px";
                    sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_bestsellers_btn.innerHTML = "";
                    sections_menu_bestsellers_btn.style.paddingRight = "250px";
                    sections_menu_bestsellers_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_brands_btn.innerHTML = "";
                    sections_menu_brands_btn.style.paddingRight = "250px";
                    sections_menu_brands_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_sale_btn.innerHTML = "";
                    sections_menu_sale_btn.style.paddingRight = "250px";
                    sections_menu_sale_btn.style.boxShadow = "0px 0px 0px #9b5de5";


                    hide_me_now_newarrival.style.display = "inline";
                    hide_me_now_bestsellers.style.display = "inline";
                    hide_me_now_brands.style.display = "inline";
                    hide_me_now_sale.style.display = "inline";






                    // sections_submenu_boys_kids_btn.style.paddingRight = "579px";
                    sections_submenu_boys_kids_btn.style.paddingRight = "100%";
                    // sections_submenu_girls_kids_btn.style.paddingRight = "580px";
                    sections_submenu_girls_kids_btn.style.paddingRight = "100%";

                }else{
                    sections_submenu_kids_ul.style.display = "none";

                    sections_ul.style.display = "flex";

                    sections_menu_women_btn.style.display = "inline";

                    sections_menu_men_btn.style.display = "inline";

                    sections_menu_newarrival_btn.innerHTML = "New.arrivals";
                    sections_menu_newarrival_btn.style.paddingRight = "140px";
                    sections_menu_newarrival_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                    sections_menu_bestsellers_btn.innerHTML = "Best.sellers";
                    sections_menu_bestsellers_btn.style.paddingRight = "144px";
                    sections_menu_bestsellers_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                    sections_menu_brands_btn.innerHTML = "Brands";
                    sections_menu_brands_btn.style.paddingRight = "183px";
                    sections_menu_brands_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                    sections_menu_sale_btn.innerHTML = "Sale";
                    sections_menu_sale_btn.style.paddingRight = "209px";
                    sections_menu_sale_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";


                    hide_me_now_newarrival.style.display = "none";
                    hide_me_now_bestsellers.style.display = "none";
                    hide_me_now_brands.style.display = "none";
                    hide_me_now_sale.style.display = "none";


                    // sections_menu_newarrival_btn.style.paddingRight = "526px";
                    sections_menu_newarrival_btn.style.paddingRight = "100%";
                    // sections_menu_bestsellers_btn.style.paddingRight = "533px";
                    sections_menu_bestsellers_btn.style.paddingRight = "100%";
                    // sections_menu_brands_btn.style.paddingRight = "569px";
                    sections_menu_brands_btn.style.paddingRight = "100%";
                    // sections_menu_sale_btn.style.paddingRight = "595px";
                    sections_menu_sale_btn.style.paddingRight = "100%";

                }
            }
            else if(sections_submenu_kids_ul.style.display == "none"){
                sections_submenu_kids_ul.style.display = "block";

                sections_submenu_boys_kids_btn.style.paddingRight = "200px";
                sections_submenu_girls_kids_btn.style.paddingRight = "200px";


                sections_menu_women_btn.style.display = "none";
                sections_menu_men_btn.style.display = "none";

                sections_ul.style.display = "block";

                sections_menu_newarrival_btn.innerHTML = "";
                sections_menu_newarrival_btn.style.paddingRight = "250px";
                sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                sections_menu_bestsellers_btn.innerHTML = "";
                sections_menu_bestsellers_btn.style.paddingRight = "250px";
                sections_menu_bestsellers_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                sections_menu_brands_btn.innerHTML = "";
                sections_menu_brands_btn.style.paddingRight = "250px";
                sections_menu_brands_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                sections_menu_sale_btn.innerHTML = "";
                sections_menu_sale_btn.style.paddingRight = "250px";
                sections_menu_sale_btn.style.boxShadow = "0px 0px 0px #9b5de5";


                hide_me_now_newarrival.style.display = "inline";
                hide_me_now_bestsellers.style.display = "inline";
                hide_me_now_brands.style.display = "inline";
                hide_me_now_sale.style.display = "inline";

            }else{
                sections_submenu_kids_ul.style.display = "none";


                sections_ul.style.display = "flex";

                sections_menu_women_btn.style.display = "inline";

                sections_menu_men_btn.style.display = "inline";

                sections_menu_newarrival_btn.innerHTML = "New.arrivals";
                sections_menu_newarrival_btn.style.paddingRight = "160px";
                sections_menu_newarrival_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                sections_menu_bestsellers_btn.innerHTML = "Best.sellers";
                sections_menu_bestsellers_btn.style.paddingRight = "160px";
                sections_menu_bestsellers_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                sections_menu_brands_btn.innerHTML = "Brands";
                sections_menu_brands_btn.style.paddingRight = "198px";
                sections_menu_brands_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                sections_menu_sale_btn.innerHTML = "Sale";
                sections_menu_sale_btn.style.paddingRight = "217px";
                sections_menu_sale_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";


                hide_me_now_newarrival.style.display = "none";
                hide_me_now_bestsellers.style.display = "none";
                hide_me_now_brands.style.display = "none";
                hide_me_now_sale.style.display = "none";

            }
        }
        kids_submenu()
        function kids_boys_subsub(){
            if(media1350px.matches){
                if(sections_subsub_boys_kids_ul.style.display == "none"){
                    sections_subsub_boys_kids_ul.style.display = "block";

                    sections_menu_newarrival_btn.innerHTML = "";
                    sections_menu_newarrival_btn.style.paddingRight = "100%";
                    sections_menu_newarrival_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                    sections_menu_bestsellers_btn.innerHTML = "";
                    sections_menu_bestsellers_btn.style.paddingRight = "100%";
                    sections_menu_bestsellers_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                    sections_menu_brands_btn.innerHTML = "";
                    sections_menu_brands_btn.style.paddingRight = "100%";
                    sections_menu_brands_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                    sections_menu_sale_btn.innerHTML = "";
                    sections_menu_sale_btn.style.paddingRight = "100%";
                    sections_menu_sale_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                }else{

                    if(sections_submenu_kids_ul.style.display != "none")
                    {
                        sections_subsub_boys_kids_ul.style.display = "none";

                        sections_menu_newarrival_btn.innerHTML = "";
                        sections_menu_newarrival_btn.style.paddingRight = "250px";
                        sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                        sections_menu_bestsellers_btn.innerHTML = "";
                        sections_menu_bestsellers_btn.style.paddingRight = "250px";
                        sections_menu_bestsellers_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                        sections_menu_brands_btn.innerHTML = "";
                        sections_menu_brands_btn.style.paddingRight = "250px";
                        sections_menu_brands_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                        sections_menu_sale_btn.innerHTML = "";
                        sections_menu_sale_btn.style.paddingRight = "250px";
                        sections_menu_sale_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    }else{
                        sections_subsub_boys_kids_ul.style.display = "none";
                    }
                }
            }
            else if(sections_subsub_boys_kids_ul.style.display == "none"){
                sections_subsub_boys_kids_ul.style.display = "block";

                sections_menu_newarrival_btn.innerHTML = "";
                sections_menu_newarrival_btn.style.paddingRight = "250px";
                sections_menu_newarrival_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                sections_menu_bestsellers_btn.innerHTML = "";
                sections_menu_bestsellers_btn.style.paddingRight = "250px";
                sections_menu_bestsellers_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                sections_menu_brands_btn.innerHTML = "";
                sections_menu_brands_btn.style.paddingRight = "250px";
                sections_menu_brands_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                sections_menu_sale_btn.innerHTML = "";
                sections_menu_sale_btn.style.paddingRight = "250px";
                sections_menu_sale_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

            }else{

                if(sections_submenu_kids_ul.style.display != "none")
                {
                    sections_subsub_boys_kids_ul.style.display = "none";

                    sections_menu_newarrival_btn.innerHTML = "";
                    sections_menu_newarrival_btn.style.paddingRight = "250px";
                    sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_bestsellers_btn.innerHTML = "";
                    sections_menu_bestsellers_btn.style.paddingRight = "250px";
                    sections_menu_bestsellers_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_brands_btn.innerHTML = "";
                    sections_menu_brands_btn.style.paddingRight = "250px";
                    sections_menu_brands_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_sale_btn.innerHTML = "";
                    sections_menu_sale_btn.style.paddingRight = "250px";
                    sections_menu_sale_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                }else{
                    sections_subsub_boys_kids_ul.style.display = "none";
                }
            }
        }
        kids_boys_subsub()
        function kids_girls_subsub(){
            if(media1350px.matches){
                if(sections_subsub_girls_kids_ul.style.display == "none"){
                    sections_subsub_girls_kids_ul.style.display = "block";

                    sections_menu_newarrival_btn.innerHTML = "";
                    sections_menu_newarrival_btn.style.paddingRight = "100%";
                    sections_menu_newarrival_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                    sections_menu_bestsellers_btn.innerHTML = "";
                    sections_menu_bestsellers_btn.style.paddingRight = "100%";
                    sections_menu_bestsellers_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                    sections_menu_brands_btn.innerHTML = "";
                    sections_menu_brands_btn.style.paddingRight = "100%";
                    sections_menu_brands_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                    sections_menu_sale_btn.innerHTML = "";
                    sections_menu_sale_btn.style.paddingRight = "100%";
                    sections_menu_sale_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                }else{

                    if(sections_submenu_kids_ul.style.display != "none")
                    {
                        sections_subsub_girls_kids_ul.style.display = "none";

                        sections_menu_newarrival_btn.innerHTML = "";
                        sections_menu_newarrival_btn.style.paddingRight = "250px";
                        sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                        sections_menu_bestsellers_btn.innerHTML = "";
                        sections_menu_bestsellers_btn.style.paddingRight = "250px";
                        sections_menu_bestsellers_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                        sections_menu_brands_btn.innerHTML = "";
                        sections_menu_brands_btn.style.paddingRight = "250px";
                        sections_menu_brands_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                        sections_menu_sale_btn.innerHTML = "";
                        sections_menu_sale_btn.style.paddingRight = "250px";
                        sections_menu_sale_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    }else{
                        sections_subsub_girls_kids_ul.style.display = "none";
                    }
                }
            }
            else if(sections_subsub_girls_kids_ul.style.display == "none"){
                sections_subsub_girls_kids_ul.style.display = "block";

                sections_menu_newarrival_btn.innerHTML = "";
                sections_menu_newarrival_btn.style.paddingRight = "250px";
                sections_menu_newarrival_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                sections_menu_bestsellers_btn.innerHTML = "";
                sections_menu_bestsellers_btn.style.paddingRight = "250px";
                sections_menu_bestsellers_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                sections_menu_brands_btn.innerHTML = "";
                sections_menu_brands_btn.style.paddingRight = "250px";
                sections_menu_brands_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                sections_menu_sale_btn.innerHTML = "";
                sections_menu_sale_btn.style.paddingRight = "250px";
                sections_menu_sale_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

            }else{

                if(sections_submenu_kids_ul.style.display != "none")
                {
                    sections_subsub_girls_kids_ul.style.display = "none";

                    sections_menu_newarrival_btn.innerHTML = "";
                    sections_menu_newarrival_btn.style.paddingRight = "250px";
                    sections_menu_newarrival_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_bestsellers_btn.innerHTML = "";
                    sections_menu_bestsellers_btn.style.paddingRight = "250px";
                    sections_menu_bestsellers_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_brands_btn.innerHTML = "";
                    sections_menu_brands_btn.style.paddingRight = "250px";
                    sections_menu_brands_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                    sections_menu_sale_btn.innerHTML = "";
                    sections_menu_sale_btn.style.paddingRight = "250px";
                    sections_menu_sale_btn.style.boxShadow = "0px 0px 0px #9b5de5";

                }else{
                    sections_subsub_girls_kids_ul.style.display = "none";
                }
            }
        }
        kids_girls_subsub()


        //new arrival section:
        function new_arrival_submenu(){
            if(media1350px.matches){
                if(sections_submenu_newarrival_ul.style.display == "none"){
                    sections_submenu_newarrival_ul.style.display = "block";

                    sections_menu_women_btn.style.display = "none";
                    sections_menu_men_btn.style.display = "none";
                    sections_menu_kids_btn.style.display = "none";

                    sections_ul.style.display = "block";

                    sections_menu_bestsellers_btn.innerHTML = "";
                    sections_menu_bestsellers_btn.style.paddingRight = "250px";
                    sections_menu_bestsellers_btn.style.boxShadow = "0px 0px 0px transparent";

                    sections_menu_brands_btn.innerHTML = "";
                    sections_menu_brands_btn.style.paddingRight = "250px";
                    sections_menu_brands_btn.style.boxShadow = "0px 0px 0px rgba(1 1 1 / 65%)";

                    sections_menu_sale_btn.innerHTML = "";
                    sections_menu_sale_btn.style.paddingRight = "250px";
                    sections_menu_sale_btn.style.boxShadow = "0px 0px 0px rgba(1 1 1 / 65%)";


                    hide_me_now_bestsellers.style.display = "inline";
                    hide_me_now_brands.style.display = "inline";
                    hide_me_now_sale.style.display = "inline";
                }else{
                    sections_submenu_newarrival_ul.style.display = "none";

                    sections_menu_women_btn.style.display = "inline";
                    sections_menu_men_btn.style.display = "inline";
                    sections_menu_kids_btn.style.display = "inline";

                    sections_ul.style.display = "flex";

                    sections_menu_bestsellers_btn.innerHTML = "Best.sellers";
                    sections_menu_bestsellers_btn.style.paddingRight = "144px";
                    sections_menu_bestsellers_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                    sections_menu_brands_btn.innerHTML = "Brands";
                    sections_menu_brands_btn.style.paddingRight = "183px";
                    sections_menu_brands_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                    sections_menu_sale_btn.innerHTML = "Sale";
                    sections_menu_sale_btn.style.paddingRight = "209px";
                    sections_menu_sale_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";


                    hide_me_now_bestsellers.style.display = "none";
                    hide_me_now_brands.style.display = "none";
                    hide_me_now_sale.style.display = "none";



                    // sections_menu_bestsellers_btn.style.paddingRight = "533px";
                    sections_menu_bestsellers_btn.style.paddingRight = "100%";
                    // sections_menu_brands_btn.style.paddingRight = "569px";
                    sections_menu_brands_btn.style.paddingRight = "100%";
                    // sections_menu_sale_btn.style.paddingRight = "595px";
                    sections_menu_sale_btn.style.paddingRight = "100%";
                }
            }
            else if(sections_submenu_newarrival_ul.style.display == "none"){
                sections_submenu_newarrival_ul.style.display = "block";

                sections_menu_women_btn.style.display = "none";
                sections_menu_men_btn.style.display = "none";
                sections_menu_kids_btn.style.display = "none";

                sections_ul.style.display = "block";

                sections_menu_bestsellers_btn.innerHTML = "";
                sections_menu_bestsellers_btn.style.paddingRight = "250px";
                sections_menu_bestsellers_btn.style.boxShadow = "0px 0px 0px transparent";

                sections_menu_brands_btn.innerHTML = "";
                sections_menu_brands_btn.style.paddingRight = "250px";
                sections_menu_brands_btn.style.boxShadow = "0px 0px 0px rgba(1 1 1 / 65%)";

                sections_menu_sale_btn.innerHTML = "";
                sections_menu_sale_btn.style.paddingRight = "250px";
                sections_menu_sale_btn.style.boxShadow = "0px 0px 0px rgba(1 1 1 / 65%)";


                hide_me_now_bestsellers.style.display = "inline";
                hide_me_now_brands.style.display = "inline";
                hide_me_now_sale.style.display = "inline";
            }else{
                sections_submenu_newarrival_ul.style.display = "none";




                sections_menu_women_btn.style.display = "inline";
                sections_menu_men_btn.style.display = "inline";
                sections_menu_kids_btn.style.display = "inline";

                sections_ul.style.display = "flex";

                sections_menu_bestsellers_btn.innerHTML = "Best.sellers";
                sections_menu_bestsellers_btn.style.paddingRight = "160px";
                sections_menu_bestsellers_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                sections_menu_brands_btn.innerHTML = "Brands";
                sections_menu_brands_btn.style.paddingRight = "198px";
                sections_menu_brands_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                sections_menu_sale_btn.innerHTML = "Sale";
                sections_menu_sale_btn.style.paddingRight = "217px";
                sections_menu_sale_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";


                hide_me_now_bestsellers.style.display = "none";
                hide_me_now_brands.style.display = "none";
                hide_me_now_sale.style.display = "none";
            }
        }
        new_arrival_submenu()
//===============================================================================================================================

        function bestsellers_submenu(){
            if(media1350px.matches){
                if(sections_submenu_bestsellers_ul.style.display == "none"){
                    sections_submenu_bestsellers_ul.style.display = "block";

                    sections_menu_women_btn.style.display = "none";
                    sections_menu_men_btn.style.display = "none";
                    sections_menu_kids_btn.style.display = "none";
                    sections_menu_newarrival_btn.style.display = "none";

                    sections_ul.style.display = "block";

                    sections_menu_brands_btn.innerHTML = "";
                    sections_menu_brands_btn.style.paddingRight = "250px";
                    sections_menu_brands_btn.style.boxShadow = "0px 0px 0px rgba(1 1 1 / 65%)";

                    sections_menu_sale_btn.innerHTML = "";
                    sections_menu_sale_btn.style.paddingRight = "250px";
                    sections_menu_sale_btn.style.boxShadow = "0px 0px 0px rgba(1 1 1 / 65%)";


                    hide_me_now_brands.style.display = "inline";
                    hide_me_now_sale.style.display = "inline";
                }else{
                    sections_submenu_bestsellers_ul.style.display = "none";
                    sections_menu_women_btn.style.display = "inline";
                    sections_menu_men_btn.style.display = "inline";
                    sections_menu_kids_btn.style.display = "inline";
                    sections_menu_newarrival_btn.style.display = "inline";

                    sections_ul.style.display = "flex";

                    sections_menu_brands_btn.innerHTML = "Brands";
                    sections_menu_brands_btn.style.paddingRight = "183px";
                    sections_menu_brands_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                    sections_menu_sale_btn.innerHTML = "Sale";
                    sections_menu_sale_btn.style.paddingRight = "209px";
                    sections_menu_sale_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";


                    hide_me_now_brands.style.display = "none";
                    hide_me_now_sale.style.display = "none";


                    // sections_menu_brands_btn.style.paddingRight = "569px";
                    sections_menu_brands_btn.style.paddingRight = "100%";
                    // sections_menu_sale_btn.style.paddingRight = "595px";
                    sections_menu_sale_btn.style.paddingRight = "100%";

                }
            }
            else if(sections_submenu_bestsellers_ul.style.display == "none"){
                sections_submenu_bestsellers_ul.style.display = "block";

                sections_menu_women_btn.style.display = "none";
                sections_menu_men_btn.style.display = "none";
                sections_menu_kids_btn.style.display = "none";
                sections_menu_newarrival_btn.style.display = "none";

                sections_ul.style.display = "block";

                sections_menu_brands_btn.innerHTML = "";
                sections_menu_brands_btn.style.paddingRight = "250px";
                sections_menu_brands_btn.style.boxShadow = "0px 0px 0px rgba(1 1 1 / 65%)";

                sections_menu_sale_btn.innerHTML = "";
                sections_menu_sale_btn.style.paddingRight = "250px";
                sections_menu_sale_btn.style.boxShadow = "0px 0px 0px rgba(1 1 1 / 65%)";


                hide_me_now_brands.style.display = "inline";
                hide_me_now_sale.style.display = "inline";
            }else{
                sections_submenu_bestsellers_ul.style.display = "none";
                sections_menu_women_btn.style.display = "inline";
                sections_menu_men_btn.style.display = "inline";
                sections_menu_kids_btn.style.display = "inline";
                sections_menu_newarrival_btn.style.display = "inline";

                sections_ul.style.display = "flex";


                sections_menu_brands_btn.innerHTML = "Brands";
                sections_menu_brands_btn.style.paddingRight = "198px";
                sections_menu_brands_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                sections_menu_sale_btn.innerHTML = "Sale";
                sections_menu_sale_btn.style.paddingRight = "217px";
                sections_menu_sale_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";


                hide_me_now_brands.style.display = "none";
                hide_me_now_sale.style.display = "none";
            }
        }
        bestsellers_submenu()

        function brands_submenu(){
            if(media1350px.matches){
                if(sections_submenu_brands_ul.style.display == "none"){
                    sections_submenu_brands_ul.style.display = "block";
                    sections_menu_women_btn.style.display = "none";
                    sections_menu_men_btn.style.display = "none";
                    sections_menu_kids_btn.style.display = "none";
                    sections_menu_newarrival_btn.style.display = "none";
                    sections_menu_bestsellers_btn.style.display = "none";

                    sections_ul.style.display = "block";

                    sections_menu_sale_btn.innerHTML = "";
                    sections_menu_sale_btn.style.paddingRight = "250px";
                    sections_menu_sale_btn.style.boxShadow = "0px 0px 0px rgba(1 1 1 / 65%)";


                    hide_me_now_sale.style.display = "inline";
                }else{
                    sections_submenu_brands_ul.style.display = "none";
                    sections_submenu_bestsellers_ul.style.display = "none";
                    sections_menu_women_btn.style.display = "inline";
                    sections_menu_men_btn.style.display = "inline";
                    sections_menu_kids_btn.style.display = "inline";
                    sections_menu_newarrival_btn.style.display = "inline";
                    sections_menu_bestsellers_btn.style.display = "inline";

                    sections_ul.style.display = "flex";

                    sections_menu_sale_btn.innerHTML = "Sale";
                    sections_menu_sale_btn.style.paddingRight = "209px";
                    sections_menu_sale_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                    hide_me_now_sale.style.display = "none";

                    // sections_menu_sale_btn.style.paddingRight = "595px";
                    sections_menu_sale_btn.style.paddingRight = "100%";

                }
            }
            else if(sections_submenu_brands_ul.style.display == "none"){
                sections_submenu_brands_ul.style.display = "block";
                sections_menu_women_btn.style.display = "none";
                sections_menu_men_btn.style.display = "none";
                sections_menu_kids_btn.style.display = "none";
                sections_menu_newarrival_btn.style.display = "none";
                sections_menu_bestsellers_btn.style.display = "none";

                sections_ul.style.display = "block";

                sections_menu_sale_btn.innerHTML = "";
                sections_menu_sale_btn.style.paddingRight = "250px";
                sections_menu_sale_btn.style.boxShadow = "0px 0px 0px rgba(1 1 1 / 65%)";


                hide_me_now_sale.style.display = "inline";
            }else{
                sections_submenu_brands_ul.style.display = "none";
                sections_submenu_bestsellers_ul.style.display = "none";
                sections_menu_women_btn.style.display = "inline";
                sections_menu_men_btn.style.display = "inline";
                sections_menu_kids_btn.style.display = "inline";
                sections_menu_newarrival_btn.style.display = "inline";
                sections_menu_bestsellers_btn.style.display = "inline";

                sections_ul.style.display = "flex";

                sections_menu_sale_btn.innerHTML = "Sale";
                sections_menu_sale_btn.style.paddingRight = "217px";
                sections_menu_sale_btn.style.boxShadow = "0px 5px 5px rgba(1 1 1 / 65%)";

                hide_me_now_sale.style.display = "none";
            }
        }
        brands_submenu()
        function sale_submenu(){
            if(sections_submenu_sale_ul.style.display == "none"){
                sections_submenu_sale_ul.style.display = "block";
                sections_menu_women_btn.style.display = "none";
                sections_menu_men_btn.style.display = "none";
                sections_menu_kids_btn.style.display = "none";
                sections_menu_newarrival_btn.style.display = "none";
                sections_menu_bestsellers_btn.style.display = "none";
                sections_menu_brands_btn.style.display = "none";

                sections_ul.style.display = "block";
            }else{
                sections_submenu_sale_ul.style.display = "none";
                sections_submenu_brands_ul.style.display = "none";
                sections_submenu_bestsellers_ul.style.display = "none";
                sections_menu_women_btn.style.display = "inline";
                sections_menu_men_btn.style.display = "inline";
                sections_menu_kids_btn.style.display = "inline";
                sections_menu_newarrival_btn.style.display = "inline";
                sections_menu_bestsellers_btn.style.display = "inline";
                sections_menu_brands_btn.style.display = "inline";

                sections_ul.style.display = "flex";
            }
        }
        sale_submenu()
    }
}

//          ====> Organizing Site Sections <====:

//              ====> sections buttons <==== :
let section_take = document.getElementById('section_take'); //input takes section name.

//              ====> women clothing <====:
let sections_women_clothing_dresses_btn = document.getElementById('sections_women_clothing_dresses_btn');
let sections_women_clothing_tops_btn = document.getElementById('sections_women_clothing_tops_btn');
let sections_women_clothing_jacketcoats_btn = document.getElementById('sections_women_clothing_jacketcoats_btn');
let sections_women_clothing_blazers_btn = document.getElementById('sections_women_clothing_blazers_btn');
let sections_women_clothing_pantsjeans_btn = document.getElementById('sections_women_clothing_pantsjeans_btn');
let sections_women_clothing_shirtsblouses_btn = document.getElementById('sections_women_clothing_shirtsblouses_btn');
let sections_women_clothing_sweetshirtshoodies_btn = document.getElementById('sections_women_clothing_sweetshirtshoodies_btn');
let sections_women_clothing_skirts_btn = document.getElementById('sections_women_clothing_skirts_btn');
let sections_women_clothing_sportwear_btn = document.getElementById('sections_women_clothing_sportwear_btn');
let sections_women_clothing_sleepwear_btn = document.getElementById('sections_women_clothing_sleepwear_btn');

//              ====> women footwears <====:
let sections_women_footwears_flats_btn = document.getElementById('sections_women_footwears_flats_btn');
let sections_women_footwears_sneakers_btn = document.getElementById('sections_women_footwears_sneakers_btn');
let sections_women_footwears_heals_btn = document.getElementById('sections_women_footwears_heals_btn');
let sections_women_footwears_boots_btn = document.getElementById('sections_women_footwears_boots_btn');
let sections_women_footwears_sandalsmules_btn = document.getElementById('sections_women_footwears_sandalsmules_btn');
let sections_women_footwears_slippers_btn = document.getElementById('sections_women_footwears_slippers_btn');

//                ====> women bags <====:
let sections_women_bags_shoulderbags_btn = document.getElementById('sections_women_bags_shoulderbags_btn');
let sections_women_bags_ClutchMinibags_btn = document.getElementById('sections_women_bags_ClutchMinibags_btn');
let sections_women_bags_tutebags_btn = document.getElementById('sections_women_bags_tutebags_btn');
let sections_women_bags_backpacks_btn = document.getElementById('sections_women_bags_backpacks_btn');
let sections_women_bags_laptopbags_btn = document.getElementById('sections_women_bags_laptopbags_btn');

//          ====> women jewelry & accessories <====:
let sections_women_jewelryandaccessories_earrings_btn = document.getElementById('sections_women_jewelryandaccessories_earrings_btn');
let sections_women_jewelryandaccessories_necklaces_btn = document.getElementById('sections_women_jewelryandaccessories_necklaces_btn');
let sections_women_jewelryandaccessories_rings_btn = document.getElementById('sections_women_jewelryandaccessories_rings_btn');
let sections_women_jewelryandaccessories_hairaccessories_btn = document.getElementById('sections_women_jewelryandaccessories_hairaccessories_btn');
let sections_women_jewelryandaccessories_phoneaccessories_btn = document.getElementById('sections_women_jewelryandaccessories_phoneaccessories_btn');

//              ====> women beauty <====:
let sections_women_beauty_bathbody_btn = document.getElementById('sections_women_beauty_bathbody_btn');
let sections_women_beauty_skincare_btn = document.getElementById('sections_women_beauty_skincare_btn');
let sections_women_beauty_haircare_btn = document.getElementById('sections_women_beauty_haircare_btn');


//===========================================================================================================
//              ====> men clothing <====:
let sections_men_clothing_sweetshirthoodies_btn = document.getElementById('sections_men_clothing_sweetshirthoodies_btn');
let sections_men_clothing_pulloversweeters_btn = document.getElementById('sections_men_clothing_pulloversweeters_btn');
let sections_men_clothing_jackets_btn = document.getElementById('sections_men_clothing_jackets_btn');
let sections_men_clothing_shirts_btn = document.getElementById('sections_men_clothing_shirts_btn');
let sections_men_clothing_tshirts_btn = document.getElementById('sections_men_clothing_tshirts_btn');
let sections_men_clothing_pantssweetpants_btn = document.getElementById('sections_men_clothing_pantssweetpants_btn');
let sections_men_clothing_sportwear_btn = document.getElementById('sections_men_clothing_sportwear_btn');
let sections_men_clothing_sleepwear_btn = document.getElementById('sections_men_clothing_sleepwear_btn');

//              ====> men footwears <====:
let sections_men_footwear_shoes_btn = document.getElementById('sections_men_footwear_shoes_btn');
let sections_men_footwear_sneakers_btn = document.getElementById('sections_men_footwear_sneakers_btn');

//              ====> men accessories <====:
let sections_men_accessories_bracelets_btn = document.getElementById('sections_men_accessories_bracelets_btn');
let sections_men_accessories_socks_btn = document.getElementById('sections_men_accessories_socks_btn');

//              ====> men beauty <====:
let sections_men_beauty_perfumes_btn = document.getElementById('sections_men_beauty_perfumes_btn');

//===========================================================================================================================
//              ====> kids boys <====:
let sections_kids_boys_sweetshirtshoodies_btn = document.getElementById('sections_kids_boys_sweetshirtshoodies_btn');
let sections_kids_boys_tshirtspolos_btn = document.getElementById('sections_kids_boys_tshirtspolos_btn');
let sections_kids_boys_pantssweetpants_btn = document.getElementById('sections_kids_boys_pantssweetpants_btn');
let sections_kids_boys_shorts_btn = document.getElementById('sections_kids_boys_shorts_btn');
let sections_kids_boys_footwears_btn = document.getElementById('sections_kids_boys_footwears_btn');

//              ====> kids girls <====:
let sections_kids_girls_tops_btn = document.getElementById('sections_kids_girls_tops_btn');
let sections_kids_girls_sweetshirtshoodies_btn = document.getElementById('sections_kids_girls_sweetshirtshoodies_btn');
let sections_kids_girls_dressesjumpsuits_btn = document.getElementById('sections_kids_girls_dressesjumpsuits_btn');
let sections_kids_girls_jacketcoats_btn = document.getElementById('sections_kids_girls_jacketcoats_btn');
let sections_kids_girls_pantssweetpants_btn = document.getElementById('sections_kids_girls_pantssweetpants_btn');
let sections_kids_girls_skirts_btn = document.getElementById('sections_kids_girls_skirts_btn');
let sections_kids_girls_footwear_btn = document.getElementById('sections_kids_girls_footwear_btn');

//=====================================================================================================================================
//                  ====> new arrival <====:
let sections_subsub_women_newarrival_btn = document.getElementById('sections_subsub_women_newarrival_btn');
let sections_subsub_men_newarrival_btn = document.getElementById('sections_subsub_men_newarrival_btn');
let sections_subsub_kids_newarrival_btn = document.getElementById('sections_subsub_kids_newarrival_btn');

//======================================================================================================================================
//                  ====> best sellers <====:
let sections_subsub_women_bestsellers_btn = document.getElementById('sections_subsub_women_bestsellers_btn');
let sections_subsub_men_bestsellers_btn = document.getElementById('sections_subsub_men_bestsellers_btn');
let sections_subsub_kids_bestsellers_btn = document.getElementById('sections_subsub_kids_bestsellers_btn');
let sections_subsub_jewelrybeauty_bestsellers_btn = document.getElementById('sections_subsub_jewelrybeauty_bestsellers_btn');

//======================================================================================================================================
//                      ====> brands <====:
let sections_subsub_calvin_brands_btn = document.getElementById('sections_subsub_calvin_brands_btn');
let sections_subsub_puma_brands_btn = document.getElementById('sections_subsub_puma_brands_btn');
let sections_subsub_lacoste_brands_btn = document.getElementById('sections_subsub_lacoste_brands_btn');
let sections_subsub_fila_brands_btn = document.getElementById('sections_subsub_fila_brands_btn');
let sections_subsub_dockers_brands_btn = document.getElementById('sections_subsub_dockers_brands_btn');

//======================================================================================================================================
//                       ====> sale <====:
let sections_subsub_sale_btn = document.getElementById('sections_subsub_sale_btn');

let creation_form = document.getElementById('creation_form');

// functions that Transfers data to the input (section_take):
if(owner){
    if(controll_pad){

        //women clothes:
        sections_women_clothing_dresses_btn.onclick = function(){
            section_take.value = "women-dresses";
            creation_form.action = creation_form.action+section_take.value;

            // creation_form.submit()
        }
        sections_women_clothing_tops_btn.onclick = function(){
            section_take.value = "women-tops";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_women_clothing_jacketcoats_btn.onclick = function(){
            section_take.value = "women-jacket&coats";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_women_clothing_blazers_btn.onclick = function(){
            section_take.value = "women-blazers";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_women_clothing_pantsjeans_btn.onclick = function(){
            section_take.value = "women-pants&jeans";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_women_clothing_shirtsblouses_btn.onclick = function(){
            section_take.value = "women-shirts&blouses";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_women_clothing_sweetshirtshoodies_btn.onclick = function(){
            section_take.value = "women-sweetshirts&hoodies";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_women_clothing_skirts_btn.onclick = function(){
            section_take.value = "women-skirts";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_women_clothing_sportwear_btn.onclick = function(){
            section_take.value = "women-sportwear";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_women_clothing_sleepwear_btn.onclick = function(){
            section_take.value = "women-sleepwear";
            creation_form.action = creation_form.action+section_take.value;
        }

        //women footwears:
        sections_women_footwears_flats_btn.onclick = function(){
            section_take.value = "women-flats";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_women_footwears_sneakers_btn.onclick = function(){
            section_take.value = "women-sneakers";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_women_footwears_heals_btn.onclick = function(){
            section_take.value = "women-heals";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_women_footwears_boots_btn.onclick = function(){
            section_take.value = "women-boots";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_women_footwears_sandalsmules_btn.onclick = function(){
            section_take.value = "women-sandals&mules";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_women_footwears_slippers_btn.onclick = function(){
            section_take.value = "women-slippers";
            creation_form.action = creation_form.action+section_take.value;
        }

        //women bags:
        sections_women_bags_shoulderbags_btn.onclick = function(){
            section_take.value = "women-shoulder_bags"
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_women_bags_ClutchMinibags_btn.onclick = function(){
            section_take.value = "women-clutch&mini_bags";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_women_bags_tutebags_btn.onclick = function(){
            section_take.value = "women-tute_bags";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_women_bags_backpacks_btn.onclick = function(){
            section_take.value = "women-back_packs";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_women_bags_laptopbags_btn.onclick = function(){
            section_take.value = "women-laptop_bags";
            creation_form.action = creation_form.action+section_take.value;
        }

        //women jewelry & accessories:
        sections_women_jewelryandaccessories_earrings_btn.onclick = function(){
            section_take.value = "women-earrings";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_women_jewelryandaccessories_necklaces_btn.onclick = function(){
            section_take.value = "women-necklaces";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_women_jewelryandaccessories_rings_btn.onclick = function(){
            section_take.value = "women-rings";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_women_jewelryandaccessories_hairaccessories_btn.onclick = function(){
            section_take.value = "women-hair_accessories";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_women_jewelryandaccessories_phoneaccessories_btn.onclick = function(){
            section_take.value = "women-phone_accessories";
            creation_form.action = creation_form.action+section_take.value;
        }

        //women beauty:
        sections_women_beauty_bathbody_btn.onclick = function(){
            section_take.value = "women-bath&body";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_women_beauty_skincare_btn.onclick = function(){
            section_take.value = "women-skincare";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_women_beauty_haircare_btn.onclick = function(){
            section_take.value = "women-haircare";
            creation_form.action = creation_form.action+section_take.value;
        }
        //=================================================
        //Men Clothing:
        sections_men_clothing_sweetshirthoodies_btn.onclick = function(){
            section_take.value = "Men-sweetshirts&hoodies";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_men_clothing_pulloversweeters_btn.onclick = function(){
            section_take.value = "Men-pullover&sweeters";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_men_clothing_jackets_btn.onclick = function(){
            section_take.value = "Men-jackets";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_men_clothing_shirts_btn.onclick = function(){
            section_take.value = "Men-shirts";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_men_clothing_tshirts_btn.onclick = function(){
            section_take.value = "Men-tshirts";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_men_clothing_pantssweetpants_btn.onclick = function(){
            section_take.value = "Men-pants&sweetpants";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_men_clothing_sportwear_btn.onclick = function(){
            section_take.value = "Men-sportwear";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_men_clothing_sleepwear_btn.onclick = function(){
            section_take.value = "Men-fullsuits";
            creation_form.action = creation_form.action+section_take.value;
        }

        // men footwears:
        sections_men_footwear_shoes_btn.onclick = function(){
            section_take.value = "Men-shoes";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_men_footwear_sneakers_btn.onclick = function(){
            section_take.value = "Men-sneakers";
            creation_form.action = creation_form.action+section_take.value;
        }

        // men accessories:
        sections_men_accessories_bracelets_btn.onclick = function(){
            section_take.value = "Men-bracelets";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_men_accessories_socks_btn.onclick = function(){
            section_take.value = "Men-socks";
            creation_form.action = creation_form.action+section_take.value;
        }

        // men beauty:
        sections_men_beauty_perfumes_btn.onclick = function(){
            section_take.value = "Men-perfumes";
            creation_form.action = creation_form.action+section_take.value;
        }
        //=============================================================================
        // Kids boys:
        sections_kids_boys_sweetshirtshoodies_btn.onclick = function(){
            section_take.value = "kids-boys_sweetshirts&hoodies";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_kids_boys_tshirtspolos_btn.onclick = function(){
            section_take.value = "kids-boys_tshirts&polos";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_kids_boys_pantssweetpants_btn.onclick = function(){
            section_take.value = "kids-boys_pants&sweetpants";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_kids_boys_shorts_btn.onclick = function(){
            section_take.value = "kids-boys_shorts";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_kids_boys_footwears_btn.onclick = function(){
            section_take.value = "kids-boys_footwears";
            creation_form.action = creation_form.action+section_take.value;
        }
        // kids girls:
        sections_kids_girls_tops_btn.onclick = function(){
            section_take.value = "kids-girls_tops";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_kids_girls_sweetshirtshoodies_btn.onclick = function(){
            section_take.value = "kids-girls_sweetshirts&hoodies";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_kids_girls_dressesjumpsuits_btn.onclick = function(){
            section_take.value = "kids-girls_dresses&jumpsuits";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_kids_girls_jacketcoats_btn.onclick = function(){
            section_take.value = "kids-girls_jacket&coats";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_kids_girls_pantssweetpants_btn.onclick = function(){
            section_take.value = "kids-girls_pants&sweetpants";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_kids_girls_skirts_btn.onclick = function(){
            section_take.value = "kids-girls_skirts";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_kids_girls_footwear_btn.onclick = function(){
            section_take.value = "kids-girls_footwear";
            creation_form.action = creation_form.action+section_take.value;
        }
        //========================================================================
        // New arrival:
        sections_subsub_women_newarrival_btn.onclick = function(){
            section_take.value = "newarrival-women";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_subsub_men_newarrival_btn.onclick = function(){
            section_take.value = "newarrival-Men";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_subsub_kids_newarrival_btn.onclick = function(){
            section_take.value = "newarrival-kids";
            creation_form.action = creation_form.action+section_take.value;
        }
        //========================================================================
        // Best sellers:
        sections_subsub_women_bestsellers_btn.onclick = function(){
            section_take.value = "bestsellers-women";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_subsub_men_bestsellers_btn.onclick = function(){
            section_take.value = "bestsellers-Men";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_subsub_kids_bestsellers_btn.onclick = function(){
            section_take.value = "bestsellers-kids";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_subsub_jewelrybeauty_bestsellers_btn.onclick = function(){
            section_take.value = "bestsellers-jewelry&beauty";
            creation_form.action = creation_form.action+section_take.value;
        }
        //========================================================================
        // Brands:
        sections_subsub_calvin_brands_btn.onclick = function(){
            section_take.value = "brands-calvin";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_subsub_puma_brands_btn.onclick = function(){
            section_take.value = "brands-puma";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_subsub_lacoste_brands_btn.onclick = function(){
            section_take.value = "brands-lacoste";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_subsub_fila_brands_btn.onclick = function(){
            section_take.value = "brands-fila";
            creation_form.action = creation_form.action+section_take.value;
        }
        sections_subsub_dockers_brands_btn.onclick = function(){
            section_take.value = "brands-dockers";
            creation_form.action = creation_form.action+section_take.value;
        }
        //========================================================================
        // Sale:
        sections_subsub_sale_btn.onclick = function(){
            section_take.value = "sale"
            creation_form.action = creation_form.action+section_take.value;
        }
    }
}







// Doing some media query things in controll pad page:
let table_view_more_btn_div = document.getElementById('table_view_more_btn_div');
let table_view_less_btn_div = document.getElementById('table_view_less_btn_div');
let table_div2 = document.getElementById('table_div2');
let table_div3 = document.getElementById('table_div3');
let small_screen_table_div = document.getElementById('small_screen_table_div');
let small_screen_table_div2 = document.getElementById('small_screen_table_div2');
let small_screen_table_view_more_btn_div = document.getElementById('small_screen_table_view_more_btn_div');
let small_screen_table_view_less_btn_div = document.getElementById('small_screen_table_view_less_btn_div');
let table_view_more_forsmall_btn_div = document.getElementById('table_view_more_forsmall_btn_div');
let table_view_less_forsmall_btn_div = document.getElementById('table_view_less_forsmall_btn_div');
let table_view_less_forsmall_btn_ForTableDiv3 = document.getElementById('table_view_less_forsmall_btn_ForTableDiv3');
let media1099px = window.matchMedia("(max-width: 1099px)");
let media420px = window.matchMedia("(min-width: 420px)");
let media419px = window.matchMedia("(max-width: 419px)");

if(owner){
    if(controll_pad){

        function show_table(){
            if (table_div2.style.display == "block"){
                table_div2.style.display = "none";
                table_div3.style.display = "block";
                // table_view_more_btn_div.style.display = "none";
                // table_view_less_btn_div.style.display = "flex";
            }else{
                table_div2.style.display = "block";
                table_div3.style.display = "none"
            }
        }
        if(media1099px.matches && media420px.matches){
            show_table();
        }






        function hide_table(){
            if (table_div3.style.display == "block"){
                table_div3.style.display = "none";
                table_div2.style.display = "block";
                // table_view_less_btn_div.style.display = "none";
                // table_view_more_btn_div.style.display = "flex";
            }
        }

        if(media1099px.matches && media420px.matches){
            hide_table();
        }




        function show_small_table(){
            if(small_screen_table_div.style.display == "block"){
                small_screen_table_div.style.display = "none";
                small_screen_table_div2.style.display = "block";
                table_view_less_forsmall_btn_div.style.display = "flex";
                table_view_more_forsmall_btn_div.style.display = "flex";
                small_screen_table_view_less_btn_div.style.display = "none";
            }else{
                small_screen_table_div.style.display = "block";
                small_screen_table_div2.style.display = "none";
            }
        }
        if(media419px.matches){
            show_small_table();
        }


        function show_small_table2(){
            if(small_screen_table_div2.style.display == "block"){
                small_screen_table_div2.style.display = "none";
                table_div3.style.display = "block";
                table_view_less_forsmall_btn_ForTableDiv3.style.display = "flex";
            }else{
                table_div3.style.display = "block";
                small_screen_table_div2.style.display = "none";
            }
        }
        if(media419px.matches){
            show_small_table2();
        }



        if(small_screen_table_view_less_btn_div){
            function hide_small_table(){
                if(table_div3.style.display == "block"){
                    table_div3.style.display = "none";
                    small_screen_table_div2.style.display = "block";
                    table_view_more_forsmall_btn_div.style.display = "flex";
                    table_view_less_forsmall_btn_div.style.display = "flex";
                    small_screen_table_view_less_btn_div.style.display = "none";
                }
            }
            hide_small_table();
        }


        if(table_view_less_forsmall_btn_div){
            function hide_small_table2(){
                if(small_screen_table_div2.style.display == "block"){
                    small_screen_table_div2.style.display = "none";
                    small_screen_table_div.style.display = "block";
                    small_screen_table_view_more_btn_div.style.display = "flex";

                }
            }
            hide_small_table2();
        }
    }
}


//showing transactions table in the controll pad:
let show_transactions_btn = document.getElementById('show_transactions_btn');
let table1 = document.getElementById('table1');
let table2 = document.getElementById('table2');
let table3 = document.getElementById('table3');
let trans_table1 = document.getElementById('trans_table1');
let trans_table_div2 = document.getElementById('trans_table_div2');
let trans_table_div3 = document.getElementById('trans_table_div3');
let trans_table2 = document.getElementById('trans_table2');
let full_trans_header = document.getElementById('full_trans_header');
let product_table_header = document.getElementById('product_table_header');
let small_screen_trans_table_div = document.getElementById('small_screen_trans_table_div');
let small_screen_trans_table_div2 = document.getElementById('small_screen_trans_table_div2');
let trans_table_view_less_forsmall_btn_div = document.getElementById('trans_table_view_less_forsmall_btn_div');
let trans_table_view_more_forsmall_btn_div = document.getElementById('trans_table_view_more_forsmall_btn_div');
let small_screen_trans_table_view_less_btn_div = document.getElementById('small_screen_trans_table_view_less_btn_div');
let trans_table_view_less_forsmall_btn_ForTableDiv3 = document.getElementById('trans_table_view_less_forsmall_btn_ForTableDiv3');
let selling_table_div2 = document.getElementById('selling_table_div2');
let best_selling_btn = document.getElementById('best_selling_btn');
let selling_table_header = document.getElementById('selling_table_header');
let selling_table1 = document.getElementById('selling_table1');
let selling_table_view_less_forsmall_btn_ForTableDiv3 = document.getElementById('selling_table_view_less_forsmall_btn_ForTableDiv3');
let small_screen_selling_table_div = document.getElementById('small_screen_selling_table_div');
let small_screen_selling_table_view_more_btn_div = document.getElementById('small_screen_selling_table_view_more_btn_div');
let small_screen_selling_table_div2 = document.getElementById('small_screen_selling_table_div2');
let selling_table_view_more_forsmall_btn_div = document.getElementById('selling_table_view_more_forsmall_btn_div');
let selling_table_div3 = document.getElementById('selling_table_div3');
let selling_table_view_less_forsmall_btn_div = document.getElementById('selling_table_view_less_forsmall_btn_div');
let small_screen_selling_table_view_less_btn_div = document.getElementById('small_screen_selling_table_view_less_btn_div');
let my_users_btn = document.getElementById('my_users_btn');
let users_table_header = document.getElementById("users_table_header");
let users_table1 = document.getElementById('users_table1');
let users_table_div2 = document.getElementById('users_table_div2');
let users_table_div3 = document.getElementById('users_table_div3');
let users_table_view_less_forsmall_btn_ForTableDiv3 = document.getElementById('users_table_view_less_forsmall_btn_ForTableDiv3');
let small_screen_users_table_div = document.getElementById('small_screen_users_table_div');
let small_screen_users_table_view_more_btn_div = document.getElementById('small_screen_users_table_view_more_btn_div');
let small_screen_users_table_div2 = document.getElementById('small_screen_users_table_div2');
let users_table_view_more_forsmall_btn_div = document.getElementById('users_table_view_more_forsmall_btn_div');
let users_table_view_less_forsmall_btn_div = document.getElementById('users_table_view_less_forsmall_btn_div');
let small_screen_users_table_view_less_btn_div = document.getElementById('small_screen_users_table_view_less_btn_div');

if(owner){
    if(controll_pad){
        function show_full_trans(){
            if(media419px.matches){

                if(small_screen_table_div.style.display == "block" || small_screen_selling_table_div.style.display == "block" ||  small_screen_users_table_div.style.display == "block"){
                    small_screen_table_div.style.display = "none";
                    small_screen_selling_table_div.style.display = "none";
                    small_screen_users_table_div.style.display = "none"
                    small_screen_trans_table_div.style.display = "block";
                    show_transactions_btn.innerText = "Hide Sales Transactions";
                    best_selling_btn.innerText = "View the best selling products";
                    my_users_btn.innerText = "Show My Users";
                }
                else if(small_screen_table_div2.style.display == "block" || small_screen_selling_table_div2.style.display == "block" || small_screen_users_table_div2.style.display == "block"){
                    small_screen_table_div2.style.display = "none";
                    small_screen_selling_table_div2.style.display = "none";
                    small_screen_users_table_div2.style.display = "none";
                    small_screen_trans_table_div2.style.display = "block";
                    small_screen_trans_table_view_less_btn_div.style.display = "none";
                    show_transactions_btn.innerText = "Hide Sales Transactions";
                    best_selling_btn.innerText = "View the best selling products";
                    my_users_btn.innerText = "Show My Users";
                    }
                else if(table_div3.style.display == "block" || selling_table_div3.style.display == "block" || users_table_div3.style.display == "block"){
                    table_div3.style.display = "none";
                    selling_table_div3.style.display = "none";
                    users_table_div3.style.display = "none";
                    trans_table_div3.style.display = "block";
                    show_transactions_btn.innerText = "Hide Sales Transactions";
                    best_selling_btn.innerText = "View the best selling products";
                    my_users_btn.innerText = "Show My Users";

                }

                else if(small_screen_trans_table_div.style.display == "block"){
                    small_screen_trans_table_div.style.display = "none";

                    small_screen_table_div.style.display = "block";
                    show_transactions_btn.innerText = "Show Sales Transactions";
                }
                else if(trans_table_div3.style.display == "block"){
                    trans_table_div3.style.display = "none";
                    table_div3.style.display = "block";
                    show_transactions_btn.innerText = "Show Sales Transactions";
                }
                else if(small_screen_trans_table_div2.style.display = "block"){
                    small_screen_trans_table_div2.style.display = "none";
                    small_screen_table_div2.style.display = "block";
                    show_transactions_btn.innerText = "Show Sales Transactions";
                }





            }
            else if(media1099px.matches && media420px.matches){
                if(table_div2.style.display == "block" || selling_table_div2.style.display == "block" || users_table_div2.style.display == "block"){
                    table_div2.style.display = "none";
                    selling_table_div2.style.display = "none";
                    users_table_div2.style.display = "none";
                    trans_table_div2.style.display = "block";
                    show_transactions_btn.innerText = "Hide Sales Transactions";
                    best_selling_btn.innerText = "View the best selling products";
                    my_users_btn.innerText = "Show My Users";
                }else{
                    trans_table_div2.style.display = "none";
                    table_div2.style.display = "block";
                    show_transactions_btn.innerText = "Show Sales Transactions";
                }
            }
            else{
                if(table1.style.display == "block" || selling_table1.style.display == "block" || users_table1.style.display == "block"){
                    table1.style.display = "none";
                    selling_table1.style.display = "none";
                    users_table1.style.display = "none";
                    product_table_header.style.display = "none";
                    show_transactions_btn.innerText = "Hide Sales Transactions";
                    best_selling_btn.innerText = "View the best selling products";
                    my_users_btn.innerText = "Show My Users";
                    trans_table1.style.display = "block";
                    full_trans_header.style.display = "block"
                    users_table_header.style.display = "none";
                    selling_table_header.style.display = "none";
                }else{
                    full_trans_header.style.display = "none";
                    trans_table1.style.display = "none";
                    show_transactions_btn.innerText = "Show Sales Transactions";
                    product_table_header.style.display = "block";
                    table1.style.display = "block";

                }
            }

        }
        if(!media1099px.matches){
            show_full_trans()
        }



        function show_trans_table(){
            if (trans_table_div2.style.display == "block"){
                trans_table_div2.style.display = "none";
                trans_table_div3.style.display = "block";
            }else{
                trans_table_div2.style.display = "block";
                trans_table_div3.style.display = "none"
            }
        }



        function hide_trans_table(){
            if (trans_table_div3.style.display == "block"){
                trans_table_div3.style.display = "none";
                trans_table_div2.style.display = "block";
            }
        }




        function show_small_trans_table(){
            if(small_screen_trans_table_div.style.display == "block"){
                small_screen_trans_table_div.style.display = "none";
                small_screen_trans_table_div2.style.display = "block";
                trans_table_view_less_forsmall_btn_div.style.display = "flex";
                trans_table_view_more_forsmall_btn_div.style.display = "flex";
                small_screen_trans_table_view_less_btn_div.style.display = "none";
            }else{
                small_screen_trans_table_div.style.display = "block";
                small_screen_trans_table_div2.style.display = "none";
            }
        }






        function show_small_trans_table2(){
            if(small_screen_trans_table_div2.style.display == "block"){
                small_screen_trans_table_div2.style.display = "none";
                trans_table_div3.style.display = "block";
                trans_table_view_less_forsmall_btn_ForTableDiv3.style.display = "flex";
            }else{
                trans_table_div3.style.display = "block";
                small_screen_trans_table_div2.style.display = "none";
            }
        }




        if(small_screen_trans_table_view_less_btn_div){
            function hide_small_trans_table(){
                if(trans_table_div3.style.display == "block"){
                    trans_table_div3.style.display = "none";
                    small_screen_trans_table_div2.style.display = "block";
                    trans_table_view_more_forsmall_btn_div.style.display = "flex";
                    trans_table_view_less_forsmall_btn_div.style.display = "flex";
                    small_screen_trans_table_view_less_btn_div.style.display = "none";
                }
            }
            hide_small_trans_table();
        }


        if(trans_table_view_less_forsmall_btn_div){
            function hide_small_trans_table2(){
                if(small_screen_trans_table_div2.style.display == "block"){
                    small_screen_trans_table_div2.style.display = "none";
                    small_screen_trans_table_div.style.display = "block";
                    small_screen_trans_table_view_more_btn_div.style.display = "flex";

                }
            }
            hide_small_trans_table2();
        }
    }
}




// Showing best selling products table at controll pad:


if(owner){
    if(controll_pad){
        function View_best_selling(){

            if(media419px.matches){
                if(small_screen_table_div.style.display == "block" || small_screen_trans_table_div.style.display == "block" || small_screen_users_table_div.style.display == "block"){
                    small_screen_table_div.style.display = "none";
                    small_screen_trans_table_div.style.display = "none";
                    small_screen_users_table_div.style.display = "none";
                    small_screen_selling_table_div.style.display = "block";
                    best_selling_btn.innerText = "Hide the best selling products";
                    show_transactions_btn.innerText = "Show Sales Transactions";
                    my_users_btn.innerText = "Show My Users";
                }
                else if(small_screen_table_div2.style.display == "block" || small_screen_trans_table_div2.style.display == "block" || small_screen_users_table_div2.style.display == "block"){
                    small_screen_table_div2.style.display = "none";
                    small_screen_trans_table_div2.style.display = "none";
                    small_screen_users_table_div2.style.display = "none";
                    small_screen_selling_table_div2.style.display = "block";
                    small_screen_selling_table_view_less_btn_div.style.display = "none";
                    best_selling_btn.innerText = "Hide the best selling products";
                    show_transactions_btn.innerText = "Show Sales Transactions";
                    my_users_btn.innerText = "Show My Users";
                    }
                else if(table_div3.style.display == "block" || trans_table_div3.style.display == "block" || users_table_div3.style.display == "block"){
                    table_div3.style.display = "none";
                    trans_table_div3.style.display = "none";
                    users_table_div3.style.display = "none";
                    selling_table_div3.style.display = "block";
                    best_selling_btn.innerText = "Hide the best selling products";
                    show_transactions_btn.innerText = "Show Sales Transactions";
                    my_users_btn.innerText = "Show My Users";
                }

                else if(small_screen_selling_table_div.style.display == "block"){
                    small_screen_selling_table_div.style.display = "none";
                    small_screen_table_div.style.display = "block";
                    best_selling_btn.innerText = "View the best selling products";
                }
                else if(selling_table_div3.style.display == "block"){
                    selling_table_div3.style.display = "none";
                    table_div3.style.display = "block";
                    best_selling_btn.innerText = "View the best selling products";
                }
                else if(small_screen_selling_table_div2.style.display = "block"){
                    small_screen_selling_table_div2.style.display = "none";
                    small_screen_table_div2.style.display = "block";
                    best_selling_btn.innerText = "View the best selling products";
                }

                // <======================>



            }
            else if(media1099px.matches && media420px.matches){
                if(table_div2.style.display == "block" || trans_table_div2.style.display == "block" || users_table_div2.style.display == "block"){
                    table_div2.style.display = "none";
                    trans_table_div2.style.display = "none";
                    users_table_div2.style.display = "none";
                    selling_table_div2.style.display = "block";
                    best_selling_btn.innerText = "Hide the best selling products";
                    show_transactions_btn.innerText = "Show Sales Transactions";
                    my_users_btn.innerText = "Show My Users";
                }else{
                    selling_table_div2.style.display = "none";
                    table_div2.style.display = "block";
                    best_selling_btn.innerText = "View the best selling products";
                }
            }


            else{
                if(table1.style.display == "block" || trans_table1.style.display == "block" || users_table1.style.display == "block"){
                    table1.style.display = "none";
                    trans_table1.style.display = "none";
                    users_table1.style.display = "none";
                    product_table_header.style.display = "none";
                    best_selling_btn.innerText = "Hide the best selling products";
                    show_transactions_btn.innerText = "Show Sales Transactions";
                    my_users_btn.innerText = "Show My Users";
                    selling_table1.style.display = "block";
                    selling_table_header.style.display = "block";
                    full_trans_header.style.display = "none";
                    users_table_header.style.display = "none";
                }else{
                    selling_table_header.style.display = "none";
                    selling_table1.style.display = "none";
                    best_selling_btn.innerText = "View the best selling products";
                    product_table_header.style.display = "block";
                    table1.style.display = "block";

                }
            }

        }



        function show_selling_table(){
            if (selling_table_div2.style.display == "block"){
                selling_table_div2.style.display = "none";
                selling_table_div3.style.display = "block";
            }else{
                selling_table_div2.style.display = "block";
                selling_table_div3.style.display = "none"
            }
        }



        function hide_selling_table(){
            if (selling_table_div3.style.display == "block"){
                selling_table_div3.style.display = "none";
                selling_table_div2.style.display = "block";
            }
        }



        function show_small_selling_table(){
            if(small_screen_selling_table_div.style.display == "block"){
                small_screen_selling_table_div.style.display = "none";
                small_screen_selling_table_div2.style.display = "block";
                selling_table_view_less_forsmall_btn_div.style.display = "flex";
                selling_table_view_more_forsmall_btn_div.style.display = "flex";
                small_screen_selling_table_view_less_btn_div.style.display = "none";
            }else{
                small_screen_selling_table_div.style.display = "block";
                small_screen_selling_table_div2.style.display = "none";
            }
        }






        function show_small_selling_table2(){
            if(small_screen_selling_table_div2.style.display == "block"){
                small_screen_selling_table_div2.style.display = "none";
                selling_table_div3.style.display = "block";
                selling_table_view_less_forsmall_btn_ForTableDiv3.style.display = "flex";
            }else{
                selling_table_div3.style.display = "block";
                small_screen_selling_table_div2.style.display = "none";
            }
        }



        if(small_screen_selling_table_view_less_btn_div){
            function hide_small_selling_table(){
                if(selling_table_div3.style.display == "block"){
                    selling_table_div3.style.display = "none";
                    small_screen_selling_table_div2.style.display = "block";
                    selling_table_view_more_forsmall_btn_div.style.display = "flex";
                    selling_table_view_less_forsmall_btn_div.style.display = "flex";
                    small_screen_selling_table_view_less_btn_div.style.display = "none";
                }
            }
            hide_small_selling_table();
        }


        if(selling_table_view_less_forsmall_btn_div){
            function hide_small_selling_table2(){
                if(small_screen_selling_table_div2.style.display == "block"){
                    small_screen_selling_table_div2.style.display = "none";
                    small_screen_selling_table_div.style.display = "block";
                    small_screen_selling_table_view_more_btn_div.style.display = "flex";

                }
            }
            hide_small_selling_table2();
        }



    }
}



if(owner){
    if(controll_pad){
        function view_users(){

            if(media419px.matches){
                if(small_screen_table_div.style.display == "block" || small_screen_trans_table_div.style.display == "block" || small_screen_selling_table_div.style.display == "block"){
                    small_screen_table_div.style.display = "none";
                    small_screen_trans_table_div.style.display = "none";
                    small_screen_selling_table_div.style.display = "none";
                    small_screen_users_table_div.style.display = "block";
                    my_users_btn.innerText = "Hide My Users";
                    best_selling_btn.innerText = "View the best selling products";
                    show_transactions_btn.innerText = "Show Sales Transactions";
                }
                else if(small_screen_table_div2.style.display == "block" || small_screen_trans_table_div2.style.display == "block" || small_screen_selling_table_div2.style.display == "block"){
                    small_screen_table_div2.style.display = "none";
                    small_screen_trans_table_div2.style.display = "none";
                    small_screen_selling_table_div2.style.display = "none";
                    small_screen_users_table_div2.style.display = "block";
                    small_screen_users_table_view_less_btn_div.style.display = "none";
                    my_users_btn.innerText = "Hide My Users";
                    best_selling_btn.innerText = "View the best selling products";
                    show_transactions_btn.innerText = "Show Sales Transactions";
                    }
                else if(table_div3.style.display == "block" || trans_table_div3.style.display == "block" || selling_table_div3.style.display == "block"){
                    table_div3.style.display = "none";
                    trans_table_div3.style.display = "none";
                    selling_table_div3.style.display = "none";
                    users_table_div3.style.display = "block";
                    my_users_btn.innerText = "Hide My Users";
                    best_selling_btn.innerText = "View the best selling products";
                    show_transactions_btn.innerText = "Show Sales Transactions";
                }

                else if(small_screen_users_table_div.style.display == "block"){
                    small_screen_users_table_div.style.display = "none";
                    small_screen_table_div.style.display = "block";
                    my_users_btn.innerText = "Show My Users";
                }
                else if(users_table_div3.style.display == "block"){
                    users_table_div3.style.display = "none";
                    table_div3.style.display = "block";
                    my_users_btn.innerText = "Show My Users";
                }
                else if(small_screen_users_table_div2.style.display = "block"){
                    small_screen_users_table_div2.style.display = "none";
                    small_screen_table_div2.style.display = "block";
                    my_users_btn.innerText = "Show My Users";
                }
            }
            else if(media1099px.matches && media420px.matches){
                if(table_div2.style.display == "block" || trans_table_div2.style.display == "block" || selling_table_div2.style.display == "block"){
                    table_div2.style.display = "none";
                    trans_table_div2.style.display = "none";
                    selling_table_div2.style.display = "none";
                    users_table_div2.style.display = "block";
                    my_users_btn.innerText = "Hide My Users";
                    best_selling_btn.innerText = "View the best selling products";
                    show_transactions_btn.innerText = "Show Sales Transactions";

                }else{
                    users_table_div2.style.display = "none";
                    table_div2.style.display = "block";
                    my_users_btn.innerText = "Show My Users";
                }
            }

            else{
                if(table1.style.display == "block" || trans_table1.style.display == "block" || selling_table1.style.display == "block"){
                    table1.style.display = "none";
                    trans_table1.style.display = "none";
                    selling_table1.style.display = "none";
                    product_table_header.style.display = "none";
                    selling_table_header.style.display = "none";
                    full_trans_header.style.display = "none";
                    my_users_btn.innerText = "Hide My Users";
                    best_selling_btn.innerText = "View the best selling products";
                    show_transactions_btn.innerText = "Show Sales Transactions";
                    users_table1.style.display = "block";
                    users_table_header.style.display = "block";
                }else{
                    users_table_header.style.display = "none";
                    users_table1.style.display = "none";
                    my_users_btn.innerText = "Show My Users";
                    product_table_header.style.display = "block";
                    table1.style.display = "block";
                }
            }

        }


        function show_users_table(){
            if (users_table_div2.style.display == "block"){
                users_table_div2.style.display = "none";
                users_table_div3.style.display = "block";
            }else{
                users_table_div2.style.display = "block";
                users_table_div3.style.display = "none"
            }
        }



        function hide_users_table(){
            if (users_table_div3.style.display == "block"){
                users_table_div3.style.display = "none";
                users_table_div2.style.display = "block";
            }
        }



        function show_small_users_table(){
            if(small_screen_users_table_div.style.display == "block"){
                small_screen_users_table_div.style.display = "none";
                small_screen_users_table_div2.style.display = "block";
                users_table_view_less_forsmall_btn_div.style.display = "flex";
                users_table_view_more_forsmall_btn_div.style.display = "flex";
                small_screen_users_table_view_less_btn_div.style.display = "none";
            }else{
                small_screen_users_table_div.style.display = "block";
                small_screen_users_table_div2.style.display = "none";
            }
        }






        function show_small_users_table2(){
            if(small_screen_users_table_div2.style.display == "block"){
                small_screen_users_table_div2.style.display = "none";
                users_table_div3.style.display = "block";
                users_table_view_less_forsmall_btn_ForTableDiv3.style.display = "flex";
            }else{
                users_table_div3.style.display = "block";
                small_screen_users_table_div2.style.display = "none";
            }
        }



        if(small_screen_users_table_view_less_btn_div){
            function hide_small_users_table(){
                if(users_table_div3.style.display == "block"){
                    users_table_div3.style.display = "none";
                    small_screen_users_table_div2.style.display = "block";
                    users_table_view_more_forsmall_btn_div.style.display = "flex";
                    users_table_view_less_forsmall_btn_div.style.display = "flex";
                    small_screen_users_table_view_less_btn_div.style.display = "none";
                }
            }
            hide_small_users_table();
        }


        if(users_table_view_less_forsmall_btn_div){
            function hide_small_users_table2(){
                if(small_screen_users_table_div2.style.display == "block"){
                    small_screen_users_table_div2.style.display = "none";
                    small_screen_users_table_div.style.display = "block";
                    small_screen_users_table_view_more_btn_div.style.display = "flex";

                }
            }
            hide_small_users_table2();
        }

    }
}






//changing product image by clicking at product page:
let slid_img1 = document.getElementById('slid_img1');
let slid_img2 = document.getElementById('slid_img2');
let slid_img3 = document.getElementById('slid_img3');
let slid_img4 = document.getElementById('slid_img4');
let slid_img5 = document.getElementById('slid_img5');
let main_img = document.getElementById('main_img');

if(slid_img1){

    slid_img1.onclick = function(){
        main_img.src = slid_img1.src;
    }

}
if(slid_img2){
    slid_img2.onclick = function(){
        main_img.src = slid_img2.src;
    }
}
if(slid_img3){
    slid_img3.onclick = function(){
        main_img.src = slid_img3.src;
    }
}
if(slid_img4){
    slid_img4.onclick = function(){
        main_img.src = slid_img4.src;
    }
}
if(slid_img5){
    slid_img5.onclick = function(){
        main_img.src = slid_img5.src;
    }
}



let message = document.getElementById('message');
if(creation){
    product_submit.onclick = function(){
        message.style.display = 'block';
    }

}



let flash1 = document.getElementById('flash1');
if(creation){
    setInterval(function(){
        flash1.style.display= 'none';
    },5000);
}


//user profile things:
let account_room_btn = document.getElementById('account_room_btn');
let account_room = document.getElementById('account_room');
let back_btn2 = document.getElementById('back_btn2');
let back_to_back_btn = document.getElementById('back_to_back');
let change_password_div = document.getElementById('change_password');
let change_pwd_btn = document.getElementById('change_pwd_btn');
let information_room_btn = document.getElementById('information_room_btn');
let information_room = document.getElementById('information_room');
let back_btn3 = document.getElementById('back_btn3');
let returns_room_btn = document.getElementById('returns_room_btn');
let returns_room = document.getElementById('returns_room');
let back_btn4 = document.getElementById('back_btn4');
let contacts_room_btn = document.getElementById('contacts_room_btn');
let contacts_room = document.getElementById('contacts_room');
let back_btn5 = document.getElementById('back_btn5');
let my_account = document.getElementById('my_account');
//            ===> Some Media Query Things              <===
let Media1259px = window.matchMedia("(max-width: 1259px)");

// Make things in the background disapear:
let Media649px = window.matchMedia("(max-width: 649px)");
// Order History things:
let order_history_btn = document.getElementById('order_history_btn');
let order_img = document.getElementById('order_img');
let order_h2 = document.getElementById('order_h2');
let order_p = document.getElementById('order_p');
// Account room things:

let account_img = document.getElementById('account_img');
let account_h2 = document.getElementById('account_h2');
let account_p = document.getElementById('account_p');
// Information room things:

let info_img = document.getElementById('info_img');
let info_h2 = document.getElementById('info_h2');
let info_p = document.getElementById('info_p');
// Returns room things:

let returns_img = document.getElementById('returns_img');
let returns_h2 = document.getElementById('returns_h2');
let returns_p = document.getElementById('returns_p');
// Contacts room things:

let contacts_img = document.getElementById('contacts_img');
let contacts_h2 = document.getElementById('contacts_h2');
let contacts_p = document.getElementById('contacts_p');
// logout room:

let logout_btn = document.getElementById('logout_btn');
let logout_img = document.getElementById('logout_img');
let logout_h2 = document.getElementById('logout_h2');
let logout_p = document.getElementById('logout_p');


if(my_account)
{
    account_room_btn.onclick = function(){
        account_room.style.top =  "350px";
    }
    back_btn2.onclick = function(){
        account_room.style.top = "850px";
    }

    if (Media1259px.matches){
        account_room_btn.onclick = function(){
            account_room.style.right =  "0px";
        }
        back_btn2.onclick = function(){
            account_room.style.right = "1300px";
        }
    }

    // make things disapear:
    if (Media649px.matches){
        account_room_btn.onclick = function(){
            account_room.style.right =  "0px";
            //order history:
            order_history_btn.style.transition = ".9s ease";
            order_history_btn.style.border = "1px solid #eee";
            order_img.style.display = "none";
            order_h2.style.transition = ".9s ease";
            order_h2.style.color = "#eee";
            order_p.style.transition = ".9s ease";
            order_p.style.color = "#eee";
            //account room:
            account_room_btn.style.transition = ".9s ease";
            account_room_btn.style.border = "1px solid #eee";
            account_img.style.display = "none";
            account_h2.style.transition = ".9s ease";
            account_h2.style.color = "#eee";
            account_p.style.transition = ".9s ease";
            account_p.style.color = "#eee";
            //Information room:
            information_room_btn.style.transition = ".9s ease";
            information_room_btn.style.border = "1px solid #eee";
            info_img.style.display = "none";
            info_h2.style.transition = ".9s ease";
            info_h2.style.color = "#eee";
            info_p.style.transition = ".9s ease";
            info_p.style.color = "#eee";
            //Returns room:
            returns_room_btn.style.transition = ".9s ease";
            returns_room_btn.style.border = "1px solid #eee";
            returns_img.style.display = "none";
            returns_h2.style.transition = ".9s ease";
            returns_h2.style.color = "#eee";
            returns_p.style.transition = ".9s ease";
            returns_p.style.color = "#eee";
            //Contacts room:
            contacts_room_btn.style.transition = ".9s ease";
            contacts_room_btn.style.border = "1px solid #eee";
            contacts_img.style.display = "none";
            contacts_h2.style.transition = ".9s ease";
            contacts_h2.style.color = "#eee";
            contacts_p.style.transition = ".9s ease";
            contacts_p.style.color = "#eee";
            //Logout room:
            logout_btn.style.transition = ".9s ease";
            logout_btn.style.border = "1px solid #eee";
            logout_img.style.display = "none";
            logout_h2.style.transition = ".9s ease";
            logout_h2.style.color = "#eee";
            logout_p.style.transition = ".9s ease";
            logout_p.style.color = "#eee";
        }
        back_btn2.onclick = function(){
            account_room.style.right = "1300px";
            //Order History:
            order_history_btn.style.transition = ".9s ease";
            order_history_btn.style.border = "1px solid black";
            order_img.style.display = "block";
            order_h2.style.transition = ".9s ease";
            order_h2.style.color = "black";
            order_p.style.transition = ".9s ease";
            order_p.style.color = "black";
            //Account room:
            account_room_btn.style.transition = ".9s ease";
            account_room_btn.style.border = "1px solid black";
            account_img.style.display = "block";
            account_h2.style.transition = ".9s ease";
            account_h2.style.color = "black";
            account_p.style.transition = ".9s ease";
            account_p.style.color = "black";
            //Information room:
            information_room_btn.style.transition = ".9s ease";
            information_room_btn.style.border = "1px solid black";
            info_img.style.display = "block";
            info_h2.style.transition = ".9s ease";
            info_h2.style.color = "black";
            info_p.style.transition = ".9s ease";
            info_p.style.color = "black";
            //Returns room:
            returns_room_btn.style.transition = ".9s ease";
            returns_room_btn.style.border = "1px solid black";
            returns_img.style.display = "block";
            returns_h2.style.transition = ".9s ease";
            returns_h2.style.color = "black";
            returns_p.style.transition = ".9s ease";
            returns_p.style.color = "black";
            //Contacts room:
            contacts_room_btn.style.transition = ".9s ease";
            contacts_room_btn.style.border = "1px solid black";
            contacts_img.style.display = "block";
            contacts_h2.style.transition = ".9s ease";
            contacts_h2.style.color = "black";
            contacts_p.style.transition = ".9s ease";
            contacts_p.style.color = "black";
            //Logout room:
            logout_btn.style.transition = ".9s ease";
            logout_btn.style.border = "1px solid black";
            logout_img.style.display = "block";
            logout_h2.style.transition = ".9s ease";
            logout_h2.style.color = "black";
            logout_p.style.transition = ".9s ease";
            logout_p.style.color = "black";
        }
    }
}


if(my_account)
{
    information_room_btn.onclick = function(){
        information_room.style.top =  "350px";
    }
    back_btn3.onclick = function(){
        information_room.style.top = "850px";
    }

    if (Media1259px.matches){
        information_room_btn.onclick = function(){
            information_room.style.right =  "0px";
        }
        back_btn3.onclick = function(){
            information_room.style.right = "1300px";
        }
    }

    // make things disapear:
    if (Media649px.matches){
        information_room_btn.onclick = function(){
            information_room.style.right =  "0px";
            //order history:
            order_history_btn.style.transition = ".9s ease";
            order_history_btn.style.border = "1px solid #eee";
            order_img.style.display = "none";
            order_h2.style.transition = ".9s ease";
            order_h2.style.color = "#eee";
            order_p.style.transition = ".9s ease";
            order_p.style.color = "#eee";
            //account room:
            account_room_btn.style.transition = ".9s ease";
            account_room_btn.style.border = "1px solid #eee";
            account_img.style.display = "none";
            account_h2.style.transition = ".9s ease";
            account_h2.style.color = "#eee";
            account_p.style.transition = ".9s ease";
            account_p.style.color = "#eee";
            //Information room:
            information_room_btn.style.transition = ".9s ease";
            information_room_btn.style.border = "1px solid #eee";
            info_img.style.display = "none";
            info_h2.style.transition = ".9s ease";
            info_h2.style.color = "#eee";
            info_p.style.transition = ".9s ease";
            info_p.style.color = "#eee";
            //Returns room:
            returns_room_btn.style.transition = ".9s ease";
            returns_room_btn.style.border = "1px solid #eee";
            returns_img.style.display = "none";
            returns_h2.style.transition = ".9s ease";
            returns_h2.style.color = "#eee";
            returns_p.style.transition = ".9s ease";
            returns_p.style.color = "#eee";
            //Contacts room:
            contacts_room_btn.style.transition = ".9s ease";
            contacts_room_btn.style.border = "1px solid #eee";
            contacts_img.style.display = "none";
            contacts_h2.style.transition = ".9s ease";
            contacts_h2.style.color = "#eee";
            contacts_p.style.transition = ".9s ease";
            contacts_p.style.color = "#eee";
            //Logout room:
            logout_btn.style.transition = ".9s ease";
            logout_btn.style.border = "1px solid #eee";
            logout_img.style.display = "none";
            logout_h2.style.transition = ".9s ease";
            logout_h2.style.color = "#eee";
            logout_p.style.transition = ".9s ease";
            logout_p.style.color = "#eee";
        }
        back_btn3.onclick = function(){
            information_room.style.right = "1300px";
            //Order History:
            order_history_btn.style.transition = ".9s ease";
            order_history_btn.style.border = "1px solid black";
            order_img.style.display = "block";
            order_h2.style.transition = ".9s ease";
            order_h2.style.color = "black";
            order_p.style.transition = ".9s ease";
            order_p.style.color = "black";
            //Account room:
            account_room_btn.style.transition = ".9s ease";
            account_room_btn.style.border = "1px solid black";
            account_img.style.display = "block";
            account_h2.style.transition = ".9s ease";
            account_h2.style.color = "black";
            account_p.style.transition = ".9s ease";
            account_p.style.color = "black";
            //Information room:
            information_room_btn.style.transition = ".9s ease";
            information_room_btn.style.border = "1px solid black";
            info_img.style.display = "block";
            info_h2.style.transition = ".9s ease";
            info_h2.style.color = "black";
            info_p.style.transition = ".9s ease";
            info_p.style.color = "black";
            //Returns room:
            returns_room_btn.style.transition = ".9s ease";
            returns_room_btn.style.border = "1px solid black";
            returns_img.style.display = "block";
            returns_h2.style.transition = ".9s ease";
            returns_h2.style.color = "black";
            returns_p.style.transition = ".9s ease";
            returns_p.style.color = "black";
            //Contacts room:
            contacts_room_btn.style.transition = ".9s ease";
            contacts_room_btn.style.border = "1px solid black";
            contacts_img.style.display = "block";
            contacts_h2.style.transition = ".9s ease";
            contacts_h2.style.color = "black";
            contacts_p.style.transition = ".9s ease";
            contacts_p.style.color = "black";
            //Logout room:
            logout_btn.style.transition = ".9s ease";
            logout_btn.style.border = "1px solid black";
            logout_img.style.display = "block";
            logout_h2.style.transition = ".9s ease";
            logout_h2.style.color = "black";
            logout_p.style.transition = ".9s ease";
            logout_p.style.color = "black";
        }
    }
}


if(my_account)
{
    returns_room_btn.onclick = function(){
        returns_room.style.top =  "350px";
    }
    back_btn4.onclick = function(){
        returns_room.style.top = "850px";
    }

    if (Media1259px.matches){
        returns_room_btn.onclick = function(){
            returns_room.style.right =  "0px";
        }
        back_btn4.onclick = function(){
            returns_room.style.right = "1300px";
        }
    }

    // make things disapear:
    if (Media649px.matches){
        returns_room_btn.onclick = function(){
            returns_room.style.right =  "0px";
            //order history:
            order_history_btn.style.transition = ".9s ease";
            order_history_btn.style.border = "1px solid #eee";
            order_img.style.display = "none";
            order_h2.style.transition = ".9s ease";
            order_h2.style.color = "#eee";
            order_p.style.transition = ".9s ease";
            order_p.style.color = "#eee";
            //account room:
            account_room_btn.style.transition = ".9s ease";
            account_room_btn.style.border = "1px solid #eee";
            account_img.style.display = "none";
            account_h2.style.transition = ".9s ease";
            account_h2.style.color = "#eee";
            account_p.style.transition = ".9s ease";
            account_p.style.color = "#eee";
            //Information room:
            information_room_btn.style.transition = ".9s ease";
            information_room_btn.style.border = "1px solid #eee";
            info_img.style.display = "none";
            info_h2.style.transition = ".9s ease";
            info_h2.style.color = "#eee";
            info_p.style.transition = ".9s ease";
            info_p.style.color = "#eee";
            //Returns room:
            returns_room_btn.style.transition = ".9s ease";
            returns_room_btn.style.border = "1px solid #eee";
            returns_img.style.display = "none";
            returns_h2.style.transition = ".9s ease";
            returns_h2.style.color = "#eee";
            returns_p.style.transition = ".9s ease";
            returns_p.style.color = "#eee";
            //Contacts room:
            contacts_room_btn.style.transition = ".9s ease";
            contacts_room_btn.style.border = "1px solid #eee";
            contacts_img.style.display = "none";
            contacts_h2.style.transition = ".9s ease";
            contacts_h2.style.color = "#eee";
            contacts_p.style.transition = ".9s ease";
            contacts_p.style.color = "#eee";
            //Logout room:
            logout_btn.style.transition = ".9s ease";
            logout_btn.style.border = "1px solid #eee";
            logout_img.style.display = "none";
            logout_h2.style.transition = ".9s ease";
            logout_h2.style.color = "#eee";
            logout_p.style.transition = ".9s ease";
            logout_p.style.color = "#eee";
        }
        back_btn4.onclick = function(){
            returns_room.style.right = "1300px";
            //Order History:
            order_history_btn.style.transition = ".9s ease";
            order_history_btn.style.border = "1px solid black";
            order_img.style.display = "block";
            order_h2.style.transition = ".9s ease";
            order_h2.style.color = "black";
            order_p.style.transition = ".9s ease";
            order_p.style.color = "black";
            //Account room:
            account_room_btn.style.transition = ".9s ease";
            account_room_btn.style.border = "1px solid black";
            account_img.style.display = "block";
            account_h2.style.transition = ".9s ease";
            account_h2.style.color = "black";
            account_p.style.transition = ".9s ease";
            account_p.style.color = "black";
            //Information room:
            information_room_btn.style.transition = ".9s ease";
            information_room_btn.style.border = "1px solid black";
            info_img.style.display = "block";
            info_h2.style.transition = ".9s ease";
            info_h2.style.color = "black";
            info_p.style.transition = ".9s ease";
            info_p.style.color = "black";
            //Returns room:
            returns_room_btn.style.transition = ".9s ease";
            returns_room_btn.style.border = "1px solid black";
            returns_img.style.display = "block";
            returns_h2.style.transition = ".9s ease";
            returns_h2.style.color = "black";
            returns_p.style.transition = ".9s ease";
            returns_p.style.color = "black";
            //Contacts room:
            contacts_room_btn.style.transition = ".9s ease";
            contacts_room_btn.style.border = "1px solid black";
            contacts_img.style.display = "block";
            contacts_h2.style.transition = ".9s ease";
            contacts_h2.style.color = "black";
            contacts_p.style.transition = ".9s ease";
            contacts_p.style.color = "black";
            //Logout room:
            logout_btn.style.transition = ".9s ease";
            logout_btn.style.border = "1px solid black";
            logout_img.style.display = "block";
            logout_h2.style.transition = ".9s ease";
            logout_h2.style.color = "black";
            logout_p.style.transition = ".9s ease";
            logout_p.style.color = "black";
        }
    }
}


if(my_account)
{
    contacts_room_btn.onclick = function(){
        contacts_room.style.top =  "350px";
    }
    back_btn5.onclick = function(){
        contacts_room.style.top = "850px";
    }

    if (Media1259px.matches){
        contacts_room_btn.onclick = function(){
            contacts_room.style.right =  "0px";
        }
        back_btn5.onclick = function(){
            contacts_room.style.right = "1300px";
        }
    }

    // make things disapear:
    if (Media649px.matches){
        contacts_room_btn.onclick = function(){
            contacts_room.style.right =  "0px";
            //order history:
            order_history_btn.style.transition = ".9s ease";
            order_history_btn.style.border = "1px solid #eee";
            order_img.style.display = "none";
            order_h2.style.transition = ".9s ease";
            order_h2.style.color = "#eee";
            order_p.style.transition = ".9s ease";
            order_p.style.color = "#eee";
            //account room:
            account_room_btn.style.transition = ".9s ease";
            account_room_btn.style.border = "1px solid #eee";
            account_img.style.display = "none";
            account_h2.style.transition = ".9s ease";
            account_h2.style.color = "#eee";
            account_p.style.transition = ".9s ease";
            account_p.style.color = "#eee";
            //Information room:
            information_room_btn.style.transition = ".9s ease";
            information_room_btn.style.border = "1px solid #eee";
            info_img.style.display = "none";
            info_h2.style.transition = ".9s ease";
            info_h2.style.color = "#eee";
            info_p.style.transition = ".9s ease";
            info_p.style.color = "#eee";
            //Returns room:
            returns_room_btn.style.transition = ".9s ease";
            returns_room_btn.style.border = "1px solid #eee";
            returns_img.style.display = "none";
            returns_h2.style.transition = ".9s ease";
            returns_h2.style.color = "#eee";
            returns_p.style.transition = ".9s ease";
            returns_p.style.color = "#eee";
            //Contacts room:
            contacts_room_btn.style.transition = ".9s ease";
            contacts_room_btn.style.border = "1px solid #eee";
            contacts_img.style.display = "none";
            contacts_h2.style.transition = ".9s ease";
            contacts_h2.style.color = "#eee";
            contacts_p.style.transition = ".9s ease";
            contacts_p.style.color = "#eee";
            //Logout room:
            logout_btn.style.transition = ".9s ease";
            logout_btn.style.border = "1px solid #eee";
            logout_img.style.display = "none";
            logout_h2.style.transition = ".9s ease";
            logout_h2.style.color = "#eee";
            logout_p.style.transition = ".9s ease";
            logout_p.style.color = "#eee";
        }
        back_btn5.onclick = function(){
            contacts_room.style.right = "1300px";
            //Order History:
            order_history_btn.style.transition = ".9s ease";
            order_history_btn.style.border = "1px solid black";
            order_img.style.display = "block";
            order_h2.style.transition = ".9s ease";
            order_h2.style.color = "black";
            order_p.style.transition = ".9s ease";
            order_p.style.color = "black";
            //Account room:
            account_room_btn.style.transition = ".9s ease";
            account_room_btn.style.border = "1px solid black";
            account_img.style.display = "block";
            account_h2.style.transition = ".9s ease";
            account_h2.style.color = "black";
            account_p.style.transition = ".9s ease";
            account_p.style.color = "black";
            //Information room:
            information_room_btn.style.transition = ".9s ease";
            information_room_btn.style.border = "1px solid black";
            info_img.style.display = "block";
            info_h2.style.transition = ".9s ease";
            info_h2.style.color = "black";
            info_p.style.transition = ".9s ease";
            info_p.style.color = "black";
            //Returns room:
            returns_room_btn.style.transition = ".9s ease";
            returns_room_btn.style.border = "1px solid black";
            returns_img.style.display = "block";
            returns_h2.style.transition = ".9s ease";
            returns_h2.style.color = "black";
            returns_p.style.transition = ".9s ease";
            returns_p.style.color = "black";
            //Contacts room:
            contacts_room_btn.style.transition = ".9s ease";
            contacts_room_btn.style.border = "1px solid black";
            contacts_img.style.display = "block";
            contacts_h2.style.transition = ".9s ease";
            contacts_h2.style.color = "black";
            contacts_p.style.transition = ".9s ease";
            contacts_p.style.color = "black";
            //Logout room:
            logout_btn.style.transition = ".9s ease";
            logout_btn.style.border = "1px solid black";
            logout_img.style.display = "block";
            logout_h2.style.transition = ".9s ease";
            logout_h2.style.color = "black";
            logout_p.style.transition = ".9s ease";
            logout_p.style.color = "black";
        }
    }
}



// transactions page things:
