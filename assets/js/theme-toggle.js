// Theme Toggle Script
(function() {
  const THEME_KEY = 'theme-preference';
  const DARK_THEME = 'dark';
  const LIGHT_THEME = 'light';

  // Get the saved theme preference or system preference
  function getThemePreference() {
    const saved = localStorage.getItem(THEME_KEY);
    if (saved) {
      return saved;
    }
    
    // Check system preference
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches) {
      return LIGHT_THEME;
    }
    
    // Default to dark
    return DARK_THEME;
  }

  // Apply theme to document
  function applyTheme(theme) {
    const html = document.documentElement;
    html.setAttribute('data-theme', theme);
    localStorage.setItem(THEME_KEY, theme);
    updateToggleButton(theme);
  }

  // Update toggle button appearance
  function updateToggleButton(theme) {
    const btn = document.getElementById('theme-toggle');
    if (btn) {
      btn.setAttribute('data-theme-current', theme);
      btn.setAttribute('aria-label', `Switch to ${theme === DARK_THEME ? 'light' : 'dark'} theme`);
      btn.textContent = theme === DARK_THEME ? '☀️' : '🌙';
    }
  }

  // Create and inject toggle button
  function createToggleButton() {
    const currentTheme = document.documentElement.getAttribute('data-theme') || DARK_THEME;
    const btn = document.createElement('button');
    btn.id = 'theme-toggle';
    btn.setAttribute('type', 'button');
    btn.textContent = currentTheme === DARK_THEME ? '☀️' : '🌙';
    btn.setAttribute('aria-label', `Switch to ${currentTheme === DARK_THEME ? 'light' : 'dark'} theme`);
    btn.onclick = function(e) {
      e.preventDefault();
      toggleTheme();
    };
    document.body.appendChild(btn);
  }

  // Initialize on page load
  function init() {
    const theme = getThemePreference();
    applyTheme(theme);
    
    // Create button immediately after applying theme
    if (!document.getElementById('theme-toggle')) {
      // Wait for DOM to be ready
      if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', createToggleButton);
      } else {
        createToggleButton();
      }
    }
  }

  // Expose toggle function
  window.toggleTheme = function() {
    const current = document.documentElement.getAttribute('data-theme') || DARK_THEME;
    const next = current === DARK_THEME ? LIGHT_THEME : DARK_THEME;
    applyTheme(next);
  };

  // Listen for system preference changes
  if (window.matchMedia) {
    window.matchMedia('(prefers-color-scheme: light)').addEventListener('change', (e) => {
      if (!localStorage.getItem(THEME_KEY)) {
        applyTheme(e.matches ? LIGHT_THEME : DARK_THEME);
      }
    });
  }

  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
