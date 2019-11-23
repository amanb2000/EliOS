// View prepared rendering
$(document).ready(() => {
    $('#welcome-text').fitText(1.1);
    $('.e-form-flow-bttn').addClass('e-form-flow-skip');
    // ADD LISTENERS
    // Create position listener to handle last link
    $('.e-form-container').scroll((e) => {
        // populate prev field with the last question
        curr = get_current_form();
        $('.e-form-faded').removeClass('e-form-faded');
        if (curr < 1) {
            $('.e-form-previous').html("");
        } else {
            targ = $(`.e-form:nth-of-type(${curr})`).children('.e-form-question');
            targ.addClass('e-form-faded');
            $('.e-form-previous').html(targ.html());
        }
        // Evauluate the skip/proceed button condition!!
        bttn = $('.e-form-flow-bttn');
        bttn.addClass('e-form-flow-skip');
        if (curr == $('.e-form').length - 1) {
            bttn.hide();
        } else {
            bttn.show();
        }
    });
});

function scroll_last() {
    // bump the scroll up a notch :) (handle 0 case too)
    curr = get_current_form();
    if (curr < 1) { return; }
    $('.e-form-container').scrollTop((curr - 1)*$('.e-form-container').height());
    return;
}

function get_current_form() {
    scrl = $('.e-form-container').scrollTop();
    height = $('.e-form-container').height();
    display = parseInt(Math.floor(scrl/height + .2));
    return display;
}

function scroll_next() {
    curr = get_current_form();
    if (curr > $('.e-form').length) { return; }
    $('.e-form-container').scrollTop((curr + 1)*$('.e-form-container').height());
    return;
}