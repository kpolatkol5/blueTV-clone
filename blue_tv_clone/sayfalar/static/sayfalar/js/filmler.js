$(".film_slider").owlCarousel({
    loop: true,
    nav: false,
    dots: false,
    responsive: {
        0: {
            items: 1
        },
        1000: {
            items: 1
        }
    }

})

$(".tüm_kategoriler_slider").owlCarousel({
    loop: true,
    nav: false,
    dots: false,
    margin: 10,
    responsive: {
        0: {
            items: 1
        },
        1000: {
            items: 6
        }
    }
})

$(".film_kategori_slide_container").owlCarousel({
    loop: true,
    nav: false,
    dots: false,
    margin: 10,
    responsive: {
        0: {
            items: 1
        },
        1000: {
            items: 5
        }
    }
})

$(document).ready(function () {
    /*
         filmlerde fare ile üzerine gelindiğinde resmin opaklığını düşürür.
    */

    $(".film_kategori_slide_container .item img").on({
        mouseenter: function () {
            $(this).css({
                "filter": "opacity(70%) ",
            })
        },
        mouseleave: (function () {
            $(this).css({
                "filter": "opacity(100%) ",
            })
        })
    })
})

$(document).ready(function () {
    /*
        filmlerde fare ile üzerine gelindiğinde info kategori gelir
    */

    $(".film_kategori_slide_container .item ").on({
        mouseenter: function (event) {

            $($(this).children()[2]).css({
                "position": "absolute",
                "bottom": "10px",
            })

            event.preventDefault();
        },

        mouseleave: (function (event) {

            $($(this).children()[2]).css({
                "position": "absolute",
                "bottom": "-40px",
            })

            event.preventDefault();
        })
    })
})

$(document).ready(function () {

    /*
        filmlerde fare ile üzerine gelindiğinde arka planın rengini koyu renk yapar
        ve child  elemanın rengini beyaz yapar
    */

    $(".film_info_btn").on({
        mouseenter: function (event) {

            $(this).css("backgroundColor", "white")
            $($(this).children()[0]).css("color", "rgb(36, 38, 48)")

            event.preventDefault();
        },

        mouseleave: function (event) {

            $(this).css("backgroundColor", "rgb(36, 38, 48)")
            $($(this).children()[0]).css("color", "white")

            event.preventDefault();
        }
    })
})

$(document).ready(function () {

    /*
        film_info_container sınıfının altındaki elemanların üzerine gelindiğinde 
        açıklama metnini getirir
    */

    // ! HATALI ÇALIŞIYOR 

    $(".film_info_container").on({

        mouseenter: function (event) {
            let element_list = $(this).children();


            let info_text = $(this).parent().children()[1];

            if (element_list[0] == event.target) {

                $(info_text).css("display", "block");
                $(info_text).html("hemen İzle");
            } else if (element_list[1] == event.target) {

                $(info_text).css("display", "block")
                $(info_text).html("Sonra İzle")
            }
        },

        mouseleave: function (event) {

            let element_list = $(this).children();
            let info_text = $(this).parent().children()[1];

            if (element_list[0] == event.target) {

                $(info_text).css("display", "none")
                $(info_text).html("hemen İzle")
            } else if (element_list[1] == event.target) {

                $(info_text).css("display", "none")
                $(info_text).html("Sonra İzle")
            }
        },

    })
})
