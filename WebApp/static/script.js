$(document).ready(function () {
    $('#calculate').click(function () {
        var units = [];
        for (var i = 1; i <= 6; i++) {
            var inputValue = $(`#unit${i}`).val().trim(); // Get the input value and trim whitespace

            // Convert the input to a number or NaN
            var numericValue = parseFloat(inputValue);

            // Check if the value is a valid number (not NaN)
            if (!isNaN(numericValue)) {
                units.push(numericValue); // Add the valid number to the array
            } else {
                $('#bill-amount').text('Please enter valid numbers.');
                return;
            }
        }

        $('#loading-indicator').show(); // Show loading indicator

        $.post('/predict', { "unit1": units[0], "unit2": units[1], "unit3": units[2], "unit4": units[3], "unit5": units[4], "unit6": units[5] }, function (data) {
            $('#loading-indicator').hide(); // Hide loading indicator
            if (data.predicted_bill) {
                $('#bill-amount').text('Total cost to produce: $' + data.predicted_bill.toFixed(2));
            } else if (data.error) {
                $('#bill-amount').text(data.error);
            }
        });
    });
});
