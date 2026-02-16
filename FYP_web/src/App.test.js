import { render, screen } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import App from './App';

test('renders home page heading', () => {
  render(
    <App />
  );
  const headingElement = screen.getByText(/3D character/i);
  expect(headingElement).toBeInTheDocument();
});