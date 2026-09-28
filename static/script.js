const chartElement = document.getElementById("predictionChart");

if (chartElement) {

    const hours = Number(
        document.getElementById("hoursData").dataset.value
    );

    const attendance = Number(
        document.getElementById("attendanceData").dataset.value
    );

    const sleep = Number(
        document.getElementById("sleepData").dataset.value
    );

    const previous = Number(
        document.getElementById("previousData").dataset.value
    );


    new Chart(chartElement, {

        type: "bar",

        data: {

            labels: [
                "Hours Studied",
                "Attendance",
                "Sleep Hours",
                "Previous Score"
            ],

            datasets: [

                {
                    label: "Student Inputs",

                    data: [
                        hours,
                        attendance,
                        sleep,
                        previous
                    ],

                    backgroundColor: [
                        "#c7ff3d",
                        "#9ed42e",
                        "#7ca91f",
                        "#5e8015"
                    ],

                    borderRadius: 8
                }

            ]
        },

        options: {

            responsive: true,

            plugins: {

                legend: {
                    labels: {
                        color: "#aaa"
                    }
                }

            },

            scales: {

                x: {
                    ticks: {
                        color: "#aaa"
                    },

                    grid: {
                        color: "#222"
                    }
                },

                y: {

                    beginAtZero: true,

                    ticks: {
                        color: "#aaa"
                    },

                    grid: {
                        color: "#222"
                    }
                }
            }
        }
    });
}