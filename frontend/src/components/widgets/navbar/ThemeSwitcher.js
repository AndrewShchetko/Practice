import React, { useState, useEffect } from 'react';
import '../../../css/theme.css'

export const ThemeSwitcher = () => {
  const [isDarkMode, setIsDarkMode] = useState(false);

  useEffect(() => {
    // Здесь вы можете использовать localStorage или другой механизм для сохранения состояния темы
    // Пример:
    // const storedTheme = localStorage.getItem('theme');
    // setIsDarkMode(storedTheme === 'dark');
  }, []);

  const toggleTheme = () => {
    setIsDarkMode((prev) => !prev);
    // Здесь вы также можете сохранить текущую тему в localStorage
    // Пример:
    // localStorage.setItem('theme', isDarkMode ? 'light' : 'dark');
  };

  return (
    <div className="text-end">
      <button className="btn btn-secondary" onClick={toggleTheme}>
        Toggle Theme
      </button>
    </div>
  );
};

