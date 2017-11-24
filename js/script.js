            // Pause the video when the modal is closed
            $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
                // Remove the src so the player itself gets removed, as this is the only
                // reliable way to ensure the video stops playing in IE
                $("#trailer-video-container").empty();
            });
            // Start playing the video whenever the trailer modal is opened
            $(document).on('click', '.movie-tile', function (event) {
                var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
                var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
                $("#trailer-video-container").empty().append($("<iframe></iframe>", {
                'id': 'trailer-video',
                'type': 'text-html',
                'src': sourceUrl,
                'frameborder': 0
                }));
            });
            function spanFollowMouse(){
                // Make .movie-tile span follow mouse when hovered.
                var tooltips = document.querySelectorAll('.movie-tile span');
            
                window.onmousemove = function (e) {
                    var x = (e.clientX + 0) + 'px',
                        y = (e.clientY + 0) + 'px';
                    for (var i = 0; i < tooltips.length; i++) {
                        tooltips[i].style.top = y;
                        tooltips[i].style.left = x;
                    }
                };
            }        
            //Animate in the movies when the page loads.    
             $(document).ready(function () {
                $('.movie-tile').hide().first().show("fast", function showNext() {
                $(this).next("div").show("fast", showNext);
                });
                //Make movie description hover over movie_tile
                spanFollowMouse();
                $("body").niceScroll({
                    cursorcolor:"#7386D5",
                    cursorwidth:"16px"
                });
                $("#sidebar").niceScroll({
                    cursorcolor:"#fff",
                    cursorwidth:"4px"
                })
                $('#sidebarCollapse').on('click', function () {
                    $('#sidebar, #content').toggleClass('active');
                    $('.collapse.in').toggleClass('in');
                    $('a[aria-expanded=true]').attr('aria-expanded', 'false');
                });
             });
