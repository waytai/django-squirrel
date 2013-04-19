function init_page() {
    $("#id_specific_target").change(function() {
        $("#target").toggle();
        $("#target").removeClass("hidden");
    });

    $("#id_regular_payins").change(function() {
        $("#repeat").toggle();
        $("#repeat").removeClass("hidden");
    })
}
