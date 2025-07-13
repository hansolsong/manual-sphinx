/**
 * MarginBook Theme JavaScript
 * Handles interactive features for the theme
 */

(function() {
    'use strict';

    // Wait for DOM to be ready
    document.addEventListener('DOMContentLoaded', function() {
        initMobileMenu();
        initMarginNotes();
        initSmoothScroll();
    });

    /**
     * Initialize mobile menu toggle
     */
    function initMobileMenu() {
        // Create mobile menu toggle button if on mobile
        if (window.innerWidth <= 768) {
            const toggleBtn = document.createElement('button');
            toggleBtn.className = 'mobile-menu-toggle';
            toggleBtn.innerHTML = '☰';
            toggleBtn.setAttribute('aria-label', 'Toggle navigation menu');
            document.body.appendChild(toggleBtn);

            const sidebar = document.querySelector('.marginbook-sidebar');

            toggleBtn.addEventListener('click', function() {
                sidebar.classList.toggle('active');
                toggleBtn.innerHTML = sidebar.classList.contains('active') ? '✕' : '☰';
            });

            // Close sidebar when clicking outside
            document.addEventListener('click', function(e) {
                if (!sidebar.contains(e.target) && !toggleBtn.contains(e.target)) {
                    sidebar.classList.remove('active');
                    toggleBtn.innerHTML = '☰';
                }
            });
        }
    }

    /**
     * Initialize margin notes positioning
     */
    function initMarginNotes() {
        const marginNotes = document.querySelectorAll('.margin-note, .sidenote, .margin-figure');

        // Position margin notes relative to their reference
        marginNotes.forEach(function(note) {
            positionMarginNote(note);
        });

        // Reposition on window resize
        let resizeTimer;
        window.addEventListener('resize', function() {
            clearTimeout(resizeTimer);
            resizeTimer = setTimeout(function() {
                marginNotes.forEach(function(note) {
                    positionMarginNote(note);
                });
            }, 250);
        });
    }

    /**
     * Position a margin note relative to its reference point
     */
    function positionMarginNote(note) {
        // Only position absolutely on larger screens
        if (window.innerWidth > 1200) {
            const prevElement = note.previousElementSibling;
            if (prevElement) {
                const rect = prevElement.getBoundingClientRect();
                const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
                note.style.top = (rect.top + scrollTop) + 'px';
            }
        } else {
            // Reset positioning for mobile
            note.style.top = '';
        }
    }

    /**
     * Initialize smooth scrolling for anchor links
     */
    function initSmoothScroll() {
        const links = document.querySelectorAll('a[href^="#"]');

        links.forEach(function(link) {
            link.addEventListener('click', function(e) {
                e.preventDefault();

                const targetId = this.getAttribute('href').slice(1);
                const targetElement = document.getElementById(targetId);

                if (targetElement) {
                    const offsetTop = targetElement.getBoundingClientRect().top + window.pageYOffset;

                    window.scrollTo({
                        top: offsetTop - 20,
                        behavior: 'smooth'
                    });
                }
            });
        });
    }

    /**
     * Utility function to debounce function calls
     */
    function debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }

})();
