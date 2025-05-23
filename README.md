# Attack Surface Profiler - Executive Dashboard

An HTML/CSS/JS dashboard that visualizes Shodan data, using D3.js for network graphs and Leaflet.js for maps. It loads data from `shodan_data_50.json` to provide insights into an organization's attack surface.

## Screenshots

Placeholder for screenshots of the Attack Surface Profiler.

## Features

- Network visualization of assets (using D3.js)
- Geographic distribution of assets (using Leaflet.js)
- KPI cards for key metrics (Total Assets, Exposed Services, Critical Vulns, Risk Score)
- Filtering by risk level, service type, and location
- Display of top vulnerabilities
- Attack vector summarization
- Executive summary section
- Modals for detailed asset and vulnerability information
- Interactive elements like attack simulation and data refresh capabilities

## Getting Started

### Prerequisites

- A modern web browser.

### Installation

1. Clone the repository (or download the `index.html`, `cleopatra.png`, and `shodan_data_50.json` files).
2. Ensure `shodan_data_50.json` and `cleopatra.png` are in the same directory as `index.html`.
3. Open `index.html` in a web browser.

### Development
Edit `index.html` for HTML/CSS/JS changes. The CSS is within `<style>` tags and JavaScript is within `<script>` tags in the `index.html` file.

## Deployment

Deploy by hosting `index.html`, `cleopatra.png`, and `shodan_data_50.json` on a static web host.

## Technology Stack

- HTML5
- CSS3 (with extensive custom styling within `index.html`)
- JavaScript (ES6+, embedded in `index.html`)
- D3.js (for network visualization)
- Leaflet.js (for geographic maps)
- `shodan_data_50.json` (for sample data)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Data visualization powered by [D3.js](https://d3js.org/) and [Leaflet.js](https://leafletjs.com/)
- Sample data from Shodan.
- Icons by [Font Awesome](https://fontawesome.com/)

## Contact

jrsherlock - [@jrsherlock](https://github.com/jrsherlock)

Project Link: [https://github.com/jrsherlock/asp_pc](https://github.com/jrsherlock/asp_pc)
