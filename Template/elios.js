// View prepared rendering
$(document).ready(() => {
    $('#welcome-text').fitText(1.1);
    // ADD LISTENERS
    // Handle calculation for scrolling
    $('.e-scroller').scroll((e) => {
        panel = $('.e-scroller');
        width = panel.width();
        scroll = panel.scrollLeft();
        display = parseInt(Math.round(scroll/width));
        // use display int to determine scroll bubble
        let cnt = 0;
        $('.e-scroll-status').children('.e-scroll-icon').each((ind, dom) => {
            elem = $(dom);
            elem.removeClass('material-icons');
            elem.removeClass('material-icons-outlined');
            if (cnt == display) {
                elem.addClass('material-icons');
            } else {
                elem.addClass('material-icons-outlined');
            }
            cnt++;
        });
    });
});

// View resize rendering
$(document).resize(() => {
    $('#welcome-text').fitText(1.1);
});