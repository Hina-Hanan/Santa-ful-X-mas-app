// UX Polish: Smooth animations and feedback

(function() {
    'use strict';

    // Character messages
    const characterMessages = {
        'elf': [
            { icon: '🔧', text: 'Great work fixing those toys!' },
            { icon: '🔧', text: 'The elves are grateful for your help!' },
            { icon: '🔧', text: 'Toy repair mission accomplished!' }
        ],
        'reindeer': [
            { icon: '🦌', text: 'Smooth navigation! The reindeer are impressed!' },
            { icon: '🦌', text: 'Excellent flying skills!' },
            { icon: '🦌', text: 'You avoided all obstacles perfectly!' }
        ],
        'ethics': [
            { icon: '🎁', text: 'A thoughtful decision. Santa approves!' },
            { icon: '🎁', text: 'Your compassion shines through!' },
            { icon: '🎁', text: 'Every choice matters. Well done!' }
        ],
        'emotion': [
            { icon: '💚', text: 'You\'ve spread joy across the world!' },
            { icon: '💚', text: 'Hearts are warmed everywhere!' },
            { icon: '💚', text: 'The world feels your kindness!' }
        ],
        'santa': [
            { icon: '🎅', text: 'Excellent progress! Keep it up!' },
            { icon: '🎅', text: 'You\'re doing wonderfully!' },
            { icon: '🎅', text: 'Christmas is in good hands!' }
        ]
    };

    // Show character message
    function showCharacterMessage(character) {
        const messages = characterMessages[character] || characterMessages['santa'];
        const message = messages[Math.floor(Math.random() * messages.length)];
        
        let messageEl = document.getElementById('character-message');
        if (!messageEl) {
            messageEl = document.createElement('div');
            messageEl.id = 'character-message';
            messageEl.className = 'character-message';
            document.body.appendChild(messageEl);
        }

        messageEl.innerHTML = `<span class="character-icon">${message.icon}</span>${message.text}`;
        messageEl.classList.add('show');

        setTimeout(() => {
            messageEl.classList.remove('show');
        }, 3000);
    }

    // Show toast notification
    function showToast(message, icon = '✓') {
        let toast = document.getElementById('toast');
        if (!toast) {
            toast = document.createElement('div');
            toast.id = 'toast';
            toast.className = 'toast';
            document.body.appendChild(toast);
        }

        toast.innerHTML = `
            <span class="toast-icon">${icon}</span>
            <span class="toast-message">${message}</span>
            <button class="toast-close" onclick="this.parentElement.classList.remove('show')">×</button>
        `;

        toast.classList.add('show');

        setTimeout(() => {
            toast.classList.remove('show');
        }, 4000);
    }

    // Animate progress bar update
    function animateProgressUpdate() {
        const progressEl = document.querySelector('.progress-percentage');
        if (progressEl) {
            progressEl.classList.add('updated');
            setTimeout(() => {
                progressEl.classList.remove('updated');
            }, 600);
        }
    }

    // Check for module completion in URL or session
    function checkForCompletion() {
        const urlParams = new URLSearchParams(window.location.search);
        const completed = urlParams.get('completed');
        
        if (completed) {
            const moduleNames = {
                'elf': 'Elf Crisis',
                'reindeer': 'Reindeer Navigation',
                'ethics': 'Gift Ethics',
                'emotion': 'Emotion Stabilizer'
            };
            
            const moduleName = moduleNames[completed];
            if (moduleName) {
                setTimeout(() => {
                    showToast(`${moduleName} completed!`, '✓');
                    showCharacterMessage(completed);
                    animateProgressUpdate();
                }, 500);
                
                // Clean URL
                window.history.replaceState({}, document.title, window.location.pathname);
            }
        }
    }

    // Smooth transitions for module cards
    function initModuleCardAnimations() {
        const cards = document.querySelectorAll('.module-card');
        cards.forEach((card, index) => {
            card.style.opacity = '0';
            card.style.transform = 'translateY(20px)';
            
            setTimeout(() => {
                card.style.transition = 'all 0.4s cubic-bezier(0.4, 0, 0.2, 1)';
                card.style.opacity = '1';
                card.style.transform = 'translateY(0)';
            }, index * 100);
        });
    }

    // Initialize on page load
    document.addEventListener('DOMContentLoaded', function() {
        checkForCompletion();
        initModuleCardAnimations();
        
        // Add smooth transitions to buttons
        const buttons = document.querySelectorAll('button, .back-button, .enter-button');
        buttons.forEach(btn => {
            btn.addEventListener('click', function(e) {
                // Add ripple effect
                const ripple = document.createElement('span');
                const rect = this.getBoundingClientRect();
                const size = Math.max(rect.width, rect.height);
                const x = e.clientX - rect.left - size / 2;
                const y = e.clientY - rect.top - size / 2;
                
                ripple.style.width = ripple.style.height = size + 'px';
                ripple.style.left = x + 'px';
                ripple.style.top = y + 'px';
                ripple.style.position = 'absolute';
                ripple.style.borderRadius = '50%';
                ripple.style.background = 'rgba(255, 255, 255, 0.3)';
                ripple.style.transform = 'scale(0)';
                ripple.style.animation = 'ripple 0.6s ease-out';
                ripple.style.pointerEvents = 'none';
                
                this.style.position = 'relative';
                this.style.overflow = 'hidden';
                this.appendChild(ripple);
                
                setTimeout(() => ripple.remove(), 600);
            });
        });
    });

    // Expose functions globally for use in templates
    window.showToast = showToast;
    window.showCharacterMessage = showCharacterMessage;
    window.animateProgressUpdate = animateProgressUpdate;
})();

// Ripple animation
const style = document.createElement('style');
style.textContent = `
    @keyframes ripple {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);
