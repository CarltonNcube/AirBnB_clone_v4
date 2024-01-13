$(document).ready(function() {
    var selectedAmenities = [];

    $('input[type="checkbox"]').change(function() {
        var amenityID = $(this).data('id');
        var amenityName = $(this).data('name');

        if ($(this).prop('checked')) {
            selectedAmenities.push(amenityID);
        } else {
            selectedAmenities = selectedAmenities.filter(function(id) {
                return id !== amenityID;
            });
        }

        $('#selected-amenities').text(selectedAmenities.join(', '));
    });
});
