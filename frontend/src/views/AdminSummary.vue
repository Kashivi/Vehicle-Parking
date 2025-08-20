<template>
  <div class="admin-summary">
    <!-- Animated Background -->
    <div class="bg-pattern"></div>
    
    <!-- Navigation Header -->
    <nav class="main-nav">
      <div class="nav-container">
        <div class="nav-brand">
          <svg viewBox="0 0 100 100" class="brand-icon">
            <rect x="10" y="20" width="80" height="60" rx="5" fill="none" stroke="currentColor" stroke-width="3"/>
            <rect x="20" y="30" width="15" height="25" rx="2" fill="currentColor"/>
            <rect x="42.5" y="30" width="15" height="25" rx="2" fill="currentColor"/>
            <rect x="65" y="30" width="15" height="25" rx="2" fill="currentColor"/>
            <text x="50" y="70" text-anchor="middle" font-size="12" fill="currentColor" font-weight="bold">P</text>
          </svg>
          <span class="brand-text">ParkSmart Admin</span>
        </div>
        
        <div class="nav-links">
          <router-link to="/admin-dashboard" class="nav-link home-link">
            <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
              <polyline points="9,22 9,12 15,12 15,22"/>
            </svg>
            Home
          </router-link>
          
          <router-link to="/user-stat" class="nav-link users-link">
            <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/>
              <circle cx="9" cy="7" r="4"/>
              <path d="M23 21v-2a4 4 0 0 0-3-3.87"/>
              <path d="M16 3.13a4 4 0 0 1 0 7.75"/>
            </svg>
            Users
          </router-link>
          
          <router-link to="/search" class="nav-link search-link">
            <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="11" cy="11" r="8"/>
              <path d="M21 21l-4.35-4.35"/>
            </svg>
            Search
          </router-link>
          
          <router-link to="/admin-summary" class="nav-link summary-link">
            <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M9 11H5a2 2 0 0 0-2 2v7a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7a2 2 0 0 0-2-2h-4"/>
              <polyline points="6,9 12,15 18,9"/>
            </svg>
            Summary
          </router-link>
          
          <router-link to="/" class="nav-link logout-link">
            <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/>
              <polyline points="16,17 21,12 16,7"/>
              <line x1="21" y1="12" x2="9" y2="12"/>
            </svg>
            Logout
          </router-link>
        </div>
      </div>
    </nav>


    <!-- Main Content -->
    <div class="main-content">
      <!-- Welcome Header -->
      <div class="welcome-section">
        <div class="welcome-content">
          <h1 class="welcome-title">
            <span class="gradient-text">Admin Analytics Dashboard 📊</span>
          </h1>
          <p class="welcome-subtitle">Comprehensive system insights and performance metrics</p>
        </div>
      </div>

      <!-- Summary Stats -->
      <div class="stats-overview">
        <div class="stat-card total-locations">
          <div class="stat-icon locations-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
              <circle cx="12" cy="10" r="3"/>
            </svg>
          </div>
          <div class="stat-content">
            <div class="stat-label">Active Locations</div>
            <div class="stat-value">{{ totalLocations }}</div>
          </div>
          <div class="stat-decoration locations-decoration"></div>
        </div>

        <div class="stat-card total-revenue">
          <div class="stat-icon revenue-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <line x1="12" y1="1" x2="12" y2="23"/>
              <path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>
            </svg>
          </div>
          <div class="stat-content">
            <div class="stat-label">Total Revenue</div>
            <div class="stat-value">₹{{ totalRevenue }}</div>
          </div>
          <div class="stat-decoration revenue-decoration"></div>
        </div>

        <div class="stat-card occupancy-rate">
          <div class="stat-icon occupancy-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M21.21 15.89A10 10 0 1 1 8 2.83"/>
              <path d="M22 12A10 10 0 0 0 12 2v10z"/>
            </svg>
          </div>
          <div class="stat-content">
            <div class="stat-label">Avg. Occupancy</div>
            <div class="stat-value">{{ occupancyRate }}%</div>
          </div>
          <div class="stat-decoration occupancy-decoration"></div>
        </div>
      </div>

      <!-- Charts Section -->
      <div class="charts-section">
        <!-- Bar Chart Card -->
        <div class="chart-card bar-chart-card">
          <div class="chart-header">
            <div class="chart-title-group">
              <div class="chart-icon bar-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <line x1="12" y1="20" x2="12" y2="10"/>
                  <line x1="18" y1="20" x2="18" y2="4"/>
                  <line x1="6" y1="20" x2="6" y2="16"/>
                </svg>
              </div>
              <div>
                <h3 class="chart-title">Revenue by Location</h3>
                <p class="chart-subtitle">Total parking revenue across all locations</p>
              </div>
            </div>
            <div class="chart-badge revenue-badge">Revenue Analysis</div>
          </div>
          <div class="chart-container">
            <canvas id="barChart" class="chart-canvas"></canvas>
          </div>
        </div>

        <!-- Pie Chart Card -->
        <div class="chart-card pie-chart-card">
          <div class="chart-header">
            <div class="chart-title-group">
              <div class="chart-icon pie-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M21.21 15.89A10 10 0 1 1 8 2.83"/>
                  <path d="M22 12A10 10 0 0 0 12 2v10z"/>
                </svg>
              </div>
              <div>
                <h3 class="chart-title">Spot Availability Status</h3>
                <p class="chart-subtitle">Real-time parking spot distribution</p>
              </div>
            </div>
            <div class="chart-badge availability-badge">Live Status</div>
          </div>
          <div class="chart-container">
            <canvas id="pieChart" class="chart-canvas"></canvas>
          </div>
        </div>
      </div>

      <!-- System Insights -->
      <div class="insights-section">
        <div class="insights-header">
          <h2 class="insights-title">
            <div class="insights-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M9 11H5a2 2 0 0 0-2 2v7a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7a2 2 0 0 0-2-2h-4"/>
                <path d="M9 11V9a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2"/>
              </svg>
            </div>
            System Insights
          </h2>
        </div>
        
        <div class="insights-grid">
          <div class="insight-card peak-location">
            <div class="insight-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
                <circle cx="12" cy="10" r="3"/>
              </svg>
            </div>
            <div class="insight-content">
              <h4>Top Revenue Location</h4>
              <p>{{ peakLocation }}</p>
            </div>
          </div>

          <div class="insight-card utilization-trend">
            <div class="insight-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="22,6 12,13 7,8 2,13"/>
                <polyline points="16,6 22,6 22,12"/>
              </svg>
            </div>
            <div class="insight-content">
              <h4>Utilization Status</h4>
              <p>{{ utilizationTrend }}</p>
            </div>
          </div>

          <div class="insight-card system-performance">
            <div class="insight-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M22 12h-4l-3 9L9 3l-3 9H2"/>
              </svg>
            </div>
            <div class="insight-content">
              <h4>System Performance</h4>
              <p>{{ systemPerformance }}</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Floating Shapes -->
      <div class="floating-shapes">
        <div class="shape shape-1"></div>
        <div class="shape shape-2"></div>
        <div class="shape shape-3"></div>
        <div class="shape shape-4"></div>
      </div>
    </div>
  </div>
</template>

<script>
import { Chart, registerables } from 'chart.js';
import ChartDataLabels from 'chartjs-plugin-datalabels';

Chart.register(...registerables, ChartDataLabels);

export default {
  name: 'AdminSummary',
  data() {
    return {
      barChart: null,
      pieChart: null,
      totalLocations: 0,
      totalRevenue: 0,
      occupancyRate: 0,
      peakLocation: '',
      utilizationTrend: '',
      systemPerformance: ''
    };
  },
  mounted() {
    this.fetchCostSummary();
    this.fetchSpotSummary();
  },
  methods: {
    async fetchCostSummary() {
      const token = localStorage.getItem("auth_token");

      try {
        const res = await fetch(`http://localhost:5000/admin/cost-summary`, {
          headers: {
            'Authorization': token
          }
        });
        const data = await res.json();

        if (Array.isArray(data) && data.length > 0) {
          const labels = data.map(item => item.location);
          const values = data.map(item => item.total_cost);
          
          // Calculate stats
          this.totalLocations = data.length;
          this.totalRevenue = values.reduce((sum, val) => sum + val, 0);
          
          // Find peak location
          const maxCost = Math.max(...values);
          this.peakLocation = data.find(item => item.total_cost === maxCost)?.location || 'N/A';
          
          this.renderBarChart(labels, values);
        }

      } catch (error) {
        console.error('Error fetching cost summary:', error);
        // Set fallback values
        this.totalLocations = 0;
        this.totalRevenue = 0;
        this.peakLocation = 'No data available';
      }
    },

    async fetchSpotSummary() {
      const token = localStorage.getItem("auth_token");

      try {
        const res = await fetch(`http://localhost:5000/admin/spot-summary`, {
          headers: {
            'Authorization': token
          }
        });
        const data = await res.json();

        if (Array.isArray(data) && data.length > 0) {
          const labels = data.map(item => item.location);
          const available = data.map(item => item.available);
          const occupied = data.map(item => item.occupied);

          // Calculate occupancy rate
          const totalAvailable = available.reduce((sum, val) => sum + val, 0);
          const totalOccupied = occupied.reduce((sum, val) => sum + val, 0);
          const totalSpots = totalAvailable + totalOccupied;
          this.occupancyRate = totalSpots > 0 ? Math.round((totalOccupied / totalSpots) * 100) : 0;

          // Generate insights
          this.generateInsights(data);

          // Prepare chart data
          const chartData = {
            labels: labels.flatMap(loc => [`${loc} (Available)`, `${loc} (Occupied)`]),
            values: labels.flatMap((_, i) => [available[i], occupied[i]])
          };

          this.renderPieChart(chartData.labels, chartData.values);
        }

      } catch (error) {
        console.error('Error fetching spot summary:', error);
        // Set fallback values
        this.occupancyRate = 0;
        this.utilizationTrend = 'No data available';
        this.systemPerformance = 'Unable to assess';
      }
    },

    generateInsights(data) {
      // Utilization trend analysis
      if (this.occupancyRate > 80) {
        this.utilizationTrend = 'High demand - Consider expansion';
      } else if (this.occupancyRate > 50) {
        this.utilizationTrend = 'Optimal utilization levels';
      } else if (this.occupancyRate > 20) {
        this.utilizationTrend = 'Moderate usage patterns';
      } else {
        this.utilizationTrend = 'Low utilization - Review pricing';
      }

      // System performance assessment
      if (this.totalRevenue > 10000) {
        this.systemPerformance = 'Excellent revenue performance';
      } else if (this.totalRevenue > 5000) {
        this.systemPerformance = 'Good system performance';
      } else if (this.totalRevenue > 1000) {
        this.systemPerformance = 'Steady growth trajectory';
      } else {
        this.systemPerformance = 'Early stage metrics';
      }
    },

    renderBarChart(labels, data) {
      const ctx = document.getElementById('barChart');

      if (this.barChart) this.barChart.destroy();

      this.barChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: labels,
          datasets: [{
            label: 'Total Revenue (₹)',
            data: data,
            backgroundColor: [
              'rgba(37, 99, 235, 0.8)',
              'rgba(139, 92, 246, 0.8)',
              'rgba(6, 182, 212, 0.8)',
              'rgba(16, 185, 129, 0.8)',
              'rgba(245, 158, 11, 0.8)',
              'rgba(236, 72, 153, 0.8)'
            ],
            borderColor: [
              'rgb(37, 99, 235)',
              'rgb(139, 92, 246)',
              'rgb(6, 182, 212)',
              'rgb(16, 185, 129)',
              'rgb(245, 158, 11)',
              'rgb(236, 72, 153)'
            ],
            borderWidth: 3,
            borderRadius: 12,
            borderSkipped: false,
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          animation: {
            duration: 2000,
            easing: 'easeOutBounce'
          },
          plugins: {
            title: {
              display: true,
              text: 'Revenue by Location',
              font: {
                size: 20,
                weight: 'bold'
              },
              color: '#1f2937',
              padding: 20
            },
            legend: {
              display: false
            }
          },
          scales: {
            y: {
              beginAtZero: true,
              grid: {
                color: 'rgba(107, 114, 128, 0.1)',
                lineWidth: 2
              },
              ticks: {
                color: '#6b7280',
                font: {
                  weight: '600',
                  size: 12
                },
                callback: function(value) {
                  return '₹' + value.toLocaleString();
                }
              }
            },
            x: {
              grid: {
                display: false
              },
              ticks: {
                color: '#6b7280',
                font: {
                  weight: '600',
                  size: 12
                }
              }
            }
          }
        }
      });
    },

    renderPieChart(labels, data) {
      const ctx = document.getElementById('pieChart');

      if (this.pieChart) this.pieChart.destroy();

      this.pieChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
          labels: labels,
          datasets: [{
            label: 'Parking Spots',
            data: data,
            backgroundColor: [
              'rgba(16, 185, 129, 0.9)',
              'rgba(239, 68, 68, 0.9)',
              'rgba(245, 158, 11, 0.9)',
              'rgba(139, 92, 246, 0.9)',
              'rgba(6, 182, 212, 0.9)',
              'rgba(236, 72, 153, 0.9)',
              'rgba(37, 99, 235, 0.9)',
              'rgba(156, 163, 175, 0.9)'
            ],
            borderColor: [
              'rgb(16, 185, 129)',
              'rgb(239, 68, 68)',
              'rgb(245, 158, 11)',
              'rgb(139, 92, 246)',
              'rgb(6, 182, 212)',
              'rgb(236, 72, 153)',
              'rgb(37, 99, 235)',
              'rgb(156, 163, 175)'
            ],
            borderWidth: 4,
            hoverOffset: 20,
            hoverBorderWidth: 6
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          animation: {
            duration: 2500,
            easing: 'easeOutBounce'
          },
          plugins: {
            title: {
              display: true,
              text: 'Parking Spot Distribution',
              font: {
                size: 20,
                weight: 'bold'
              },
              color: '#1f2937',
              padding: 20
            },
            legend: {
              position: 'bottom',
              labels: {
                padding: 25,
                usePointStyle: true,
                pointStyle: 'circle',
                font: {
                  size: 13,
                  weight: '600'
                },
                color: '#6b7280'
              }
            },
            datalabels: {
              color: '#fff',
              formatter: (value, ctx) => {
                if (value === 0) return '';
                return value;
              },
              font: {
                weight: 'bold',
                size: 14
              }
            }
          },
          cutout: '65%'
        }
      });
    }
  }
};
</script>

<style scoped>
/* Color Variables - Admin Theme */
:root {
  --primary-blue: #2563eb;      
  --secondary-blue: #3b82f6;    
  --accent-orange: #f59e0b;     
  --accent-purple: #8b5cf6;     
  --success-green: #10b981;     
  --pink-accent: #ec4899;       
  --cyan-accent: #06b6d4;       
  --red-accent: #ef4444;        
  --dark-gray: #1f2937;         
  --medium-gray: #6b7280;       
  --light-gray: #f3f4f6;        
  --white: #ffffff;
  --shadow: rgba(0, 0, 0, 0.1);
  --shadow-dark: rgba(0, 0, 0, 0.2);
}

.admin-summary {
  min-height: 100vh;
  background: linear-gradient(135deg, 
    var(--primary-blue) 0%, 
    var(--accent-purple) 25%, 
    var(--pink-accent) 50%, 
    var(--cyan-accent) 75%, 
    var(--success-green) 100%);
  background-size: 400% 400%;
  animation: gradientShift 15s ease infinite;
  position: relative;
  padding-bottom: 40px;
}

@keyframes gradientShift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

/* Animated Background Pattern */
.bg-pattern {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: 
    radial-gradient(circle at 20% 30%, rgba(255, 255, 255, 0.1) 0%, transparent 50%),
    radial-gradient(circle at 80% 70%, rgba(245, 158, 11, 0.1) 0%, transparent 50%),
    radial-gradient(circle at 60% 20%, rgba(139, 92, 246, 0.1) 0%, transparent 50%),
    repeating-linear-gradient(
      45deg,
      transparent,
      transparent 80px,
      rgba(255, 255, 255, 0.02) 82px,
      rgba(255, 255, 255, 0.02) 84px
    );
  animation: drift 25s linear infinite;
  pointer-events: none;
}

@keyframes drift {
  0% { transform: translate(0, 0) rotate(0deg); }
  100% { transform: translate(50px, 50px) rotate(360deg); }
}

/* Navigation */
.main-nav {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  border-bottom: 2px solid transparent;
  background-image: linear-gradient(rgba(255, 255, 255, 0.95), rgba(255, 255, 255, 0.95)),
                    linear-gradient(90deg, var(--success-green), var(--cyan-accent), var(--accent-orange));
  background-origin: border-box;
  background-clip: content-box, border-box;
  padding: 15px 0;
  position: sticky;
  top: 0;
  z-index: 100;
  box-shadow: 0 8px 32px var(--shadow);
}

.nav-container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
}

.nav-brand {
  display: flex;
  align-items: center;
  gap: 12px;
}

.brand-icon {
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, var(--primary-blue), var(--accent-purple));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: brandPulse 4s ease-in-out infinite;
}

@keyframes brandPulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.05); }
}

.brand-text {
  font-size: 1.8em;
  font-weight: 800;
  background: linear-gradient(135deg, var(--primary-blue), var(--accent-purple));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  background-color: black;
}

.nav-links {
  display: flex;
  gap: 8px;
  align-items: center;
}

.nav-link {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 20px;
  text-decoration: none;
  color: var(--medium-gray);
  font-weight: 600;
  border-radius: 12px;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.nav-icon {
  width: 18px;
  height: 18px;
}

.nav-link:hover {
  color: var(--white);
  transform: translateY(-2px);
}

.home-link:hover { background: linear-gradient(135deg, var(--primary-blue), var(--secondary-blue)); }
.users-link:hover { background: linear-gradient(135deg, var(--accent-purple), var(--pink-accent)); }
.search-link:hover { background: linear-gradient(135deg, var(--cyan-accent), var(--success-green)); }
.summary-link:hover { background: linear-gradient(135deg, var(--accent-orange), var(--pink-accent)); }
.logout-link:hover { background: linear-gradient(135deg, var(--red-accent), var(--pink-accent)); }

.nav-link.router-link-exact-active {
  background: linear-gradient(135deg, var(--primary-blue), var(--accent-purple));
  color: var(--white);
  box-shadow: 0 4px 15px rgba(37, 99, 235, 0.3);
}

/* Main Content */
.main-content {
  max-width: 1400px;
  margin: 0 auto;
  padding: 40px 30px;
  position: relative;
  z-index: 1;
}

/* Welcome Section */
.welcome-section {
  text-align: center;
  margin-bottom: 50px;
  animation: fadeInUp 0.8s ease-out;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.welcome-title {
  font-size: 3em;
  font-weight: 800;
  margin-bottom: 15px;
  letter-spacing: -1px;
}

.gradient-text {
  color: #000;
  text-shadow: 0 2px 3px rgba(0, 0, 0, 0.2);
}

.welcome-subtitle {
  color: rgb(0, 0, 0);
  font-size: 1.2em;
  font-weight: 500;
}

/* Stats Overview */
.stats-overview {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 30px;
  margin-bottom: 50px;
  animation: slideInLeft 0.8s ease-out 0.2s both;
}

@keyframes slideInLeft {
  from {
    opacity: 0;
    transform: translateX(-50px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.stat-card {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(15px);
  border-radius: 24px;
  padding: 35px;
  display: flex;
  align-items: center;
  gap: 25px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  box-shadow: 0 15px 50px var(--shadow-dark);
  position: relative;
  overflow: hidden;
  transition: all 0.4s ease;
  animation: cardFloat 4s ease-in-out infinite;
}

@keyframes cardFloat {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-8px); }
}

.stat-card:hover {
  transform: translateY(-12px) scale(1.03);
  box-shadow: 0 30px 80px var(--shadow-dark);
}

.stat-icon {
  width: 70px;
  height: 70px;
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--white);
  position: relative;
  animation: iconPulse 3s ease-in-out infinite;
}

@keyframes iconPulse {
  0%, 100% { transform: scale(1) rotate(0deg); }
  50% { transform: scale(1.1) rotate(5deg); }
}

.locations-icon {
  background: linear-gradient(135deg, var(--success-green), var(--cyan-accent));
}

.revenue-icon {
  background: linear-gradient(135deg, var(--accent-orange), var(--pink-accent));
}

.occupancy-icon {
  background: linear-gradient(135deg, var(--primary-blue), var(--accent-purple));
}

.stat-icon svg {
  width: 32px;
  height: 32px;
}

.stat-content {
  flex: 1;
}

.stat-label {
  font-size: 1.1em;
  font-weight: 600;
  color: var(--medium-gray);
  margin-bottom: 8px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.stat-value {
  font-size: 2.8em;
  font-weight: 800;
  background: linear-gradient(135deg, var(--primary-blue), var(--accent-purple));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: valueCount 2s ease-out;
  background-color: #000;
}

@keyframes valueCount {
  from { transform: scale(0.5); opacity: 0; }
  to { transform: scale(1); opacity: 1; }
}

.stat-decoration {
  position: absolute;
  top: -15px;
  right: -15px;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  opacity: 0.2;
  animation: decorationFloat 5s ease-in-out infinite;
}

@keyframes decorationFloat {
  0%, 100% { transform: translate(0, 0) rotate(0deg); }
  25% { transform: translate(5px, -5px) rotate(90deg); }
  50% { transform: translate(-5px, -10px) rotate(180deg); }
  75% { transform: translate(-10px, 5px) rotate(270deg); }
}

.locations-decoration {
  background: linear-gradient(135deg, var(--success-green), var(--cyan-accent));
}

.revenue-decoration {
  background: linear-gradient(135deg, var(--accent-orange), var(--pink-accent));
}

.occupancy-decoration {
  background: linear-gradient(135deg, var(--primary-blue), var(--accent-purple));
}

/* Charts Section */
.charts-section {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
  gap: 40px;
  margin-bottom: 50px;
  animation: slideInRight 0.8s ease-out 0.4s both;
}

@keyframes slideInRight {
  from {
    opacity: 0;
    transform: translateX(50px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.chart-card {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(15px);
  border-radius: 24px;
  padding: 35px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  box-shadow: 0 20px 60px var(--shadow-dark);
  position: relative;
  overflow: hidden;
  transition: all 0.4s ease;
}

.chart-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 5px;
  background: linear-gradient(90deg, 
    var(--primary-blue), 
    var(--accent-purple), 
    var(--pink-accent), 
    var(--cyan-accent), 
    var(--success-green));
  background-size: 300% 300%;
  animation: borderShimmer 4s ease infinite;
}

@keyframes borderShimmer {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}

.chart-card:hover {
  transform: translateY(-8px) scale(1.02);
  box-shadow: 0 30px 90px var(--shadow-dark);
}

.chart-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 30px;
}

.chart-title-group {
  display: flex;
  align-items: center;
  gap: 20px;
}

.chart-icon {
  width: 50px;
  height: 50px;
  border-radius: 15px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--white);
  animation: chartIconSpin 4s ease-in-out infinite;
}

@keyframes chartIconSpin {
  0%, 100% { transform: rotate(0deg) scale(1); }
  25% { transform: rotate(5deg) scale(1.05); }
  50% { transform: rotate(0deg) scale(1.1); }
  75% { transform: rotate(-5deg) scale(1.05); }
}

.bar-icon {
  background: linear-gradient(135deg, var(--accent-orange), var(--pink-accent));
}

.pie-icon {
  background: linear-gradient(135deg, var(--success-green), var(--cyan-accent));
}

.chart-icon svg {
  width: 24px;
  height: 24px;
}

.chart-title {
  font-size: 1.6em;
  font-weight: 700;
  color: var(--dark-gray);
  margin: 0 0 5px 0;
}

.chart-subtitle {
  color: var(--medium-gray);
  font-size: 1em;
  font-weight: 500;
  margin: 0;
}

.chart-badge {
  padding: 10px 18px;
  border-radius: 20px;
  font-weight: 700;
  font-size: 0.85em;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  animation: badgePulse 3s ease-in-out infinite;
}

@keyframes badgePulse {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.05); opacity: 0.9; }
}

.revenue-badge {
  background: linear-gradient(135deg, rgba(245, 158, 11, 0.15), rgba(236, 72, 153, 0.15));
  color: var(--accent-orange);
  border: 2px solid rgba(245, 158, 11, 0.3);
}

.availability-badge {
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.15), rgba(6, 182, 212, 0.15));
  color: var(--success-green);
  border: 2px solid rgba(16, 185, 129, 0.3);
}

.chart-container {
  position: relative;
  height: 400px;
  padding: 20px;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(243, 244, 246, 0.1));
  border-radius: 16px;
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.chart-canvas {
  width: 100% !important;
  height: 100% !important;
}

/* Insights Section */
.insights-section {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(15px);
  border-radius: 24px;
  padding: 40px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  box-shadow: 0 20px 60px var(--shadow-dark);
  position: relative;
  overflow: hidden;
  animation: fadeIn 0.8s ease-out 0.6s both;
}

@keyframes fadeIn {
  from { opacity: 0; transform: scale(0.95); }
  to { opacity: 1; transform: scale(1); }
}

.insights-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 5px;
  background: linear-gradient(90deg, 
    var(--success-green), 
    var(--cyan-accent), 
    var(--primary-blue), 
    var(--accent-purple), 
    var(--pink-accent));
  background-size: 300% 300%;
  animation: borderShimmer 4s ease infinite;
}

.insights-header {
  text-align: center;
  margin-bottom: 40px;
}

.insights-title {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 15px;
  font-size: 2em;
  font-weight: 700;
  color: var(--dark-gray);
  margin: 0;
}

.insights-icon {
  width: 50px;
  height: 50px;
  background: linear-gradient(135deg, var(--accent-orange), var(--pink-accent));
  border-radius: 15px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--white);
  animation: iconSparkle 2s ease-in-out infinite;
}

@keyframes iconSparkle {
  0%, 100% { transform: scale(1) rotate(0deg); filter: brightness(1); }
  25% { transform: scale(1.1) rotate(5deg); filter: brightness(1.2); }
  50% { transform: scale(1.05) rotate(0deg); filter: brightness(1.1); }
  75% { transform: scale(1.1) rotate(-5deg); filter: brightness(1.2); }
}

.insights-icon svg {
  width: 24px;
  height: 24px;
}

.insights-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 25px;
}

.insight-card {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.9), rgba(243, 244, 246, 0.9));
  border-radius: 20px;
  padding: 25px;
  border: 2px solid rgba(255, 255, 255, 0.4);
  box-shadow: 0 10px 40px var(--shadow);
  transition: all 0.4s ease;
  position: relative;
  overflow: hidden;
}

.insight-card::after {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, 
    transparent, 
    rgba(255, 255, 255, 0.3), 
    transparent);
  transition: left 0.6s ease;
}

.insight-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 20px 60px var(--shadow-dark);
  border-color: rgba(37, 99, 235, 0.4);
}

.insight-card:hover::after {
  left: 100%;
}

.insight-card .insight-icon {
  width: 50px;
  height: 50px;
  border-radius: 15px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--white);
  margin-bottom: 15px;
  animation: insightIconFloat 3s ease-in-out infinite;
}

@keyframes insightIconFloat {
  0%, 100% { transform: translateY(0px) rotate(0deg); }
  50% { transform: translateY(-3px) rotate(3deg); }
}

.peak-location .insight-icon {
  background: linear-gradient(135deg, var(--success-green), var(--cyan-accent));
}

.utilization-trend .insight-icon {
  background: linear-gradient(135deg, var(--accent-orange), var(--pink-accent));
}

.system-performance .insight-icon {
  background: linear-gradient(135deg, var(--primary-blue), var(--accent-purple));
}

.insight-icon svg {
  width: 24px;
  height: 24px;
}

.insight-content h4 {
  font-size: 1.3em;
  font-weight: 700;
  color: var(--dark-gray);
  margin: 0 0 8px 0;
}

.insight-content p {
  color: var(--medium-gray);
  font-size: 1.1em;
  font-weight: 600;
  margin: 0;
}

/* Floating Shapes */
.floating-shapes {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
  z-index: 0;
}

.shape {
  position: absolute;
  border-radius: 50%;
  opacity: 0.08;
}

.shape-1 {
  width: 120px;
  height: 120px;
  top: 15%;
  right: 8%;
  background: linear-gradient(135deg, var(--success-green), var(--cyan-accent));
  animation: floatShape1 15s ease-in-out infinite;
}

.shape-2 {
  width: 80px;
  height: 80px;
  bottom: 25%;
  left: 5%;
  background: linear-gradient(135deg, var(--accent-orange), var(--pink-accent));
  animation: floatShape2 12s ease-in-out infinite;
}

.shape-3 {
  width: 100px;
  height: 100px;
  top: 55%;
  right: 20%;
  background: linear-gradient(135deg, var(--accent-purple), var(--primary-blue));
  animation: floatShape3 18s ease-in-out infinite;
}

.shape-4 {
  width: 140px;
  height: 140px;
  bottom: 5%;
  right: 2%;
  background: linear-gradient(135deg, var(--pink-accent), var(--cyan-accent));
  animation: floatShape4 20s ease-in-out infinite;
}

@keyframes floatShape1 {
  0%, 100% { transform: translate(0, 0) rotate(0deg); }
  25% { transform: translate(40px, -30px) rotate(90deg); }
  50% { transform: translate(-20px, -50px) rotate(180deg); }
  75% { transform: translate(-35px, 20px) rotate(270deg); }
}

@keyframes floatShape2 {
  0%, 100% { transform: translate(0, 0) rotate(0deg); }
  33% { transform: translate(35px, -25px) rotate(120deg); }
  66% { transform: translate(-25px, -35px) rotate(240deg); }
}

@keyframes floatShape3 {
  0%, 100% { transform: translate(0, 0) rotate(0deg); }
  50% { transform: translate(30px, -40px) rotate(180deg); }
}

@keyframes floatShape4 {
  0%, 100% { transform: translate(0, 0) rotate(0deg); }
  25% { transform: translate(-30px, -35px) rotate(90deg); }
  50% { transform: translate(25px, -55px) rotate(180deg); }
  75% { transform: translate(45px, 15px) rotate(270deg); }
}

/* Responsive Design */
@media (max-width: 1200px) {
  .charts-section {
    grid-template-columns: 1fr;
    gap: 30px;
  }
}

@media (max-width: 768px) {
  .main-content {
    padding: 30px 20px;
  }
  
  .welcome-title {
    font-size: 2.2em;
  }
  
  .stats-overview {
    grid-template-columns: 1fr;
    gap: 20px;
  }
  
  .chart-card {
    padding: 25px 20px;
  }
  
  .chart-container {
    height: 300px;
  }
  
  .nav-container {
    flex-direction: column;
    gap: 20px;
    padding: 0 20px;
  }
  
  .nav-links {
    flex-wrap: wrap;
    justify-content: center;
  }
  
  .insights-grid {
    grid-template-columns: 1fr;
  }
  
  .chart-header {
    flex-direction: column;
    gap: 15px;
    align-items: flex-start;
  }
  
  .chart-title-group {
    gap: 15px;
  }
}

@media (max-width: 480px) {
  .welcome-title {
    font-size: 1.8em;
  }
  
  .stat-card {
    padding: 25px 20px;
    flex-direction: column;
    text-align: center;
    gap: 15px;
  }
  
  .chart-card {
    padding: 20px 15px;
  }
  
  .chart-container {
    height: 250px;
    padding: 15px;
  }
  
  .insights-section {
    padding: 30px 20px;
  }
  
  .nav-link {
    padding: 8px 12px;
    font-size: 0.85em;
  }
  
  .nav-icon {
    width: 16px;
    height: 16px;
  }
  
  .stat-icon {
    width: 60px;
    height: 60px;
  }
  
  .stat-value {
    font-size: 2.2em;
  }
}

/* Loading States */
.loading-chart {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 300px;
  color: var(--medium-gray);
  font-size: 1.2em;
  font-weight: 600;
}

.loading-spinner {
  width: 40px;
  height: 40px;
  border: 4px solid rgba(37, 99, 235, 0.2);
  border-top: 4px solid var(--primary-blue);
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-right: 15px;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* Focus States for Accessibility */
.nav-link:focus {
  outline: 3px solid var(--accent-orange);
  outline-offset: 2px;
}

/* Enhanced Hover Effects */
.chart-title-group:hover .chart-icon {
  transform: scale(1.1) rotate(10deg);
}

.stat-card:hover .stat-icon {
  transform: scale(1.15) rotate(10deg);
}

.insight-card:hover .insight-icon {
  transform: scale(1.1) rotate(5deg);
}

/* Smooth Transitions */
* {
  transition: transform 0.3s ease, box-shadow 0.3s ease, color 0.3s ease;
}

/* Custom Scrollbar */
::-webkit-scrollbar {
  width: 8px;
}

::-webkit-scrollbar-track {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 10px;
}

::-webkit-scrollbar-thumb {
  background: linear-gradient(135deg, var(--primary-blue), var(--accent-purple));
  border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
  background: linear-gradient(135deg, var(--accent-purple), var(--pink-accent));
}
</style>