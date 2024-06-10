document.addEventListener('DOMContentLoaded', function() {
    function updateTimer() {
        fetch('/get_timer')
            .then(response => response.json())
            .then(data => {
                document.getElementById('timer').textContent = data.remaining_time;
            });
    }

    setInterval(updateTimer, 1000);
});
