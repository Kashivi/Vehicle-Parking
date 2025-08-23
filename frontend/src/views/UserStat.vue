<template>
  <div v-if="isAdmin" class="user-stats">
    <!-- Background Pattern -->
    <div class="bg-pattern"></div>
    ->
      <!-- Navigation Section -->
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

    <div class="user-stats-header">
        <h1 class="user-stats-title">
          <span class="gradient-text">User Management</span>
        </h1>
        <p class="user-stats-subtitle">Registered users overview and statistics</p>
      </div>

      <!-- Stats Cards -->
      <div class="stats-section">
        <div class="stats-card">
          <div class="stat-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/>
              <circle cx="9" cy="7" r="4"/>
              <path d="M23 21v-2a4 4 0 0 0-3-3.87"/>
              <path d="M16 3.13a4 4 0 0 1 0 7.75"/>
            </svg>
          </div>
          <div class="stat-content">
            <div class="stat-number">{{ users.length }}</div>
            <div class="stat-label">Total Users</div>
          </div>
          <div class="stat-shimmer"></div>
        </div>
      </div>

      <!-- Users Table Section -->
      <div class="table-section">
        <div class="table-header">
          <h3 class="table-title">
            <svg class="table-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/>
              <rect x="8" y="2" width="8" height="4" rx="1" ry="1"/>
            </svg>
            Registered Users
          </h3>
        </div>

        <!-- Loading State -->
        <div v-if="loading" class="loading-state">
          <div class="loading-spinner large"></div>
          <p class="loading-text">Loading users...</p>
        </div>

        <!-- Error State -->
        <div v-else-if="error" class="error-state">
          <div class="error-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="12" cy="12" r="10"/>
              <line x1="15" y1="9" x2="9" y2="15"/>
              <line x1="9" y1="9" x2="15" y2="15"/>
            </svg>
          </div>
          <p class="error-message">{{ error }}</p>
        </div>

        <!-- Users Table -->
        <div v-else class="table-wrapper">
          <table class="modern-table" v-if="users.length > 0">
            <thead>
              <tr>
                <th>
                  <div class="th-content">
                    <svg class="th-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <path d="M9 12l2 2 4-4"/>
                      <path d="M21 12c-1 0-3-1-3-3s2-3 3-3 3 1 3 3-2 3-3 3"/>
                      <path d="M3 12c1 0 3-1 3-3s-2-3-3-3-3 1-3 3 2 3 3 3"/>
                    </svg>
                    ID
                  </div>
                </th>
                <th>
                  <div class="th-content">
                    <svg class="th-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
                      <circle cx="12" cy="7" r="4"/>
                    </svg>
                    Username
                  </div>
                </th>
                <th>
                  <div class="th-content">
                    <svg class="th-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
                      <polyline points="22,6 12,13 2,6"/>
                    </svg>
                    Email
                  </div>
                </th>
                <th>
                  <div class="th-content">
                    <svg class="th-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
                      <circle cx="12" cy="10" r="3"/>
                    </svg>
                    Address
                  </div>
                </th>
                <th>
                  <div class="th-content">
                    <svg class="th-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
                    </svg>
                    Phone
                  </div>
                </th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(user, index) in users" :key="user.id" class="table-row" :style="{ animationDelay: (index * 0.1) + 's' }">
                <td>
                  <div class="user-id">{{ user.id }}</div>
                </td>
                <td>
                  <div class="user-info">
                    <div class="user-avatar">
                      {{ user.username.charAt(0).toUpperCase() }}
                    </div>
                    <div class="username">{{ user.username }}</div>
                  </div>
                </td>
                <td>
                  <div class="user-email">{{ user.email }}</div>
                </td>
                <td>
                  <div class="user-address">{{ user.address || 'Not provided' }}</div>
                </td>
                <td>
                  <div class="user-phone">{{ user.phone_number || 'Not provided' }}</div>
                </td>
              </tr>
            </tbody>
          </table>

          <!-- Empty State -->
          <div v-else class="empty-state">
            <div class="empty-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/>
                <circle cx="9" cy="7" r="4"/>
                <path d="M23 21v-2a4 4 0 0 0-3-3.87"/>
                <path d="M16 3.13a4 4 0 0 1 0 7.75"/>
              </svg>
            </div>
            <h3 class="empty-title">No Users Found</h3>
            <p class="empty-description">There are currently no registered users in the system.</p>
          </div>
        </div>
      </div>

      <!-- Decorative Elements -->
      <div class="floating-shapes">
        <div class="shape shape-1"></div>
        <div class="shape shape-2"></div>
        <div class="shape shape-3"></div>
        <div class="shape shape-4"></div>
      </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'UserStat',
  data() {
    return {
      users: [],
      loading: false,
      error: null,
      isAdmin: false
    }
  },
  mounted() {
    const user = JSON.parse(localStorage.getItem('user') || '{}')
    const token = localStorage.getItem('auth_token')
    this.isAdmin = token && user.role === 'admin'

    if (!this.isAdmin) {
      this.$router.replace('/')
    } else {
      this.fetchUsers()
    }
  },
  methods: {
    formatDate(dt) {
      return new Date(dt).toLocaleString()
    },
    async fetchUsers() {
      this.loading = true
      this.error = null

      try {
        const token = localStorage.getItem('auth_token')
        const res = await axios.get('http://127.0.0.1:5000/api/userinfo', {
          headers: {
            Authorization: `Bearer ${token}`
          }
        })
        const data = res.data
        if (Array.isArray(data.users)) {
          this.users = data.users
        } else {
          this.error = data.message || 'Invalid response format.'
        }
      } catch (e) {
        console.error(e)
        this.error = e.response?.data?.message || 'Network/server error'
      } finally {
        this.loading = false
      }
    }
  }
}
</script>

<style scoped>
/* Color Variables - Vibrant Admin Theme */
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

.user-stats {
  min-height: 100vh;
  background: linear-gradient(135deg, 
    var(--accent-purple) 0%, 
    var(--primary-blue) 25%, 
    var(--cyan-accent) 50%, 
    var(--success-green) 75%, 
    var(--accent-orange) 100%);
  background-size: 400% 400%;
  animation: gradientShift 12s ease infinite;
  padding: 30px 20px;
  position: relative;
  overflow-x: hidden;
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
    radial-gradient(circle at 25% 25%, rgba(255, 255, 255, 0.1) 0%, transparent 50%),
    radial-gradient(circle at 75% 75%, rgba(245, 158, 11, 0.1) 0%, transparent 50%),
    radial-gradient(circle at 50% 50%, rgba(139, 92, 246, 0.1) 0%, transparent 50%),
    repeating-linear-gradient(
      45deg,
      transparent,
      transparent 100px,
      rgba(255, 255, 255, 0.02) 102px,
      rgba(255, 255, 255, 0.02) 104px
    );
  animation: drift 25s linear infinite, pulse 8s ease-in-out infinite;
}

@keyframes drift {
  0% { transform: translate(0, 0) rotate(0deg); }
  100% { transform: translate(50px, 50px) rotate(360deg); }
}

@keyframes pulse {
  0%, 100% { opacity: 0.5; }
  50% { opacity: 1; }
}

/* Main Container */
.user-stats-container {
  max-width: 1200px;
  margin: 0 auto;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  border-radius: 28px;
  padding: 50px 40px;
  box-shadow: 
    0 30px 100px var(--shadow-dark),
    0 0 0 1px rgba(255, 255, 255, 0.2),
    inset 0 1px 0 rgba(255, 255, 255, 0.9);
  border: 1px solid rgba(255, 255, 255, 0.3);
  position: relative;
  z-index: 1;
  animation: slideUp 0.8s ease-out;
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(60px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Header Section */
.user-stats-header {
  text-align: center;
  margin-bottom: 40px;
}

.admin-icon {
  display: inline-block;
  margin-bottom: 20px;
  background: linear-gradient(135deg, var(--accent-orange), var(--pink-accent), var(--accent-purple));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: float 4s ease-in-out infinite, colorRotate 10s ease infinite;
}

.admin-icon .icon {
  width: 70px;
  height: 70px;
  filter: drop-shadow(0 6px 15px rgba(245, 158, 11, 0.5));
}

@keyframes float {
  0%, 100% { transform: translateY(0px) rotate(0deg); }
  50% { transform: translateY(-10px) rotate(5deg); }
}

@keyframes colorRotate {
  0%, 100% { filter: drop-shadow(0 6px 15px rgba(245, 158, 11, 0.5)) hue-rotate(0deg); }
  33% { filter: drop-shadow(0 6px 15px rgba(236, 72, 153, 0.5)) hue-rotate(120deg); }
  66% { filter: drop-shadow(0 6px 15px rgba(139, 92, 246, 0.5)) hue-rotate(240deg); }
}

.user-stats-title {
  font-size: 2.6em;
  font-weight: 900;
  margin-bottom: 12px;
  letter-spacing: -1.5px;
}

.gradient-text {
  color: #000;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
}

@keyframes textShimmer {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}

.user-stats-subtitle {
  color: var(--medium-gray);
  font-size: 1.2em;
  font-weight: 500;
}

/* Navigation Section */
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


/* Stats Section */
.stats-section {
  margin-bottom: 40px;
  animation: fadeInUp 0.8s ease-out 0.4s both;
}

.stats-card {
  display: flex;
  align-items: center;
  gap: 20px;
  background: linear-gradient(135deg, 
    rgba(16, 185, 129, 0.1) 0%, 
    rgba(6, 182, 212, 0.1) 100%);
  padding: 30px;
  border-radius: 20px;
  border: 2px solid var(--success-green);
  position: relative;
  overflow: hidden;
  box-shadow: 0 15px 40px rgba(16, 185, 129, 0.2);
  transition: all 0.3s ease;
  max-width: 300px;
}

.stats-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 25px 60px rgba(16, 185, 129, 0.3);
}

.stat-icon {
  width: 60px;
  height: 60px;
  background: linear-gradient(135deg, var(--success-green), var(--cyan-accent));
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--white);
  box-shadow: 0 8px 25px rgba(16, 185, 129, 0.3);
  animation: iconFloat 3s ease-in-out infinite;
}

@keyframes iconFloat {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-5px); }
}

.stat-icon svg {
  width: 30px;
  height: 30px;
}

.stat-content {
  flex: 1;
}

.stat-number {
  font-size: 2em;
  font-weight: 800;
  color: var(--dark-gray);
}

.stat-label {
  font-size: 1em;
  font-weight: 600;
  color: var(--medium-gray);
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.stat-shimmer {
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, 
    transparent, 
    rgba(255, 255, 255, 0.3), 
    transparent);
  animation: shimmer 4s ease-in-out infinite;
}

@keyframes shimmer {
  0% { left: -100%; }
  100% { left: 100%; }
}

/* Table Section */
.table-section {
  animation: fadeInUp 0.8s ease-out 0.6s both;
}

.table-header {
  margin-bottom: 25px;
}

.table-title {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 1.6em;
  font-weight: 700;
  color: var(--dark-gray);
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.table-icon {
  width: 28px;
  height: 28px;
  color: var(--accent-orange);
  animation: iconPulse 2.5s ease-in-out infinite;
}

@keyframes iconPulse {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.1); opacity: 0.8; }
}

/* Loading State */
.loading-state {
  text-align: center;
  padding: 60px 20px;
}

.loading-spinner {
  width: 40px;
  height: 40px;
  border: 4px solid rgba(245, 158, 11, 0.3);
  border-top: 4px solid var(--accent-orange);
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 20px;
}

.loading-spinner.large {
  width: 60px;
  height: 60px;
  border-width: 5px;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.loading-text {
  font-size: 1.2em;
  font-weight: 600;
  color: var(--medium-gray);
}

/* Error State */
.error-state {
  text-align: center;
  padding: 60px 20px;
}

.error-icon {
  width: 60px;
  height: 60px;
  background: linear-gradient(135deg, var(--red-accent), var(--pink-accent));
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--white);
  margin: 0 auto 20px;
  box-shadow: 0 10px 30px rgba(239, 68, 68, 0.3);
}

.error-icon svg {
  width: 30px;
  height: 30px;
}

.error-message {
  font-size: 1.2em;
  font-weight: 600;
  color: var(--red-accent);
}

/* Table Wrapper */
.table-wrapper {
  background: var(--white);
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 15px 50px var(--shadow-dark);
  border: 1px solid rgba(255, 255, 255, 0.5);
}

.modern-table {
  width: 100%;
  border-collapse: collapse;
  font-family: inherit;
}

.modern-table thead {
  background: linear-gradient(135deg, 
    var(--dark-gray) 0%, 
    var(--medium-gray) 100%);
  color: var(--white);
}

.modern-table th {
  padding: 20px 24px;
  text-align: left;
  font-weight: 700;
  font-size: 0.9em;
  text-transform: uppercase;
  letter-spacing: 1px;
  position: relative;
  border-bottom: 3px solid var(--accent-orange);
}

.th-content {
  display: flex;
  align-items: center;
  gap: 8px;
}

.th-icon {
  width: 16px;
  height: 16px;
  opacity: 0.9;
}

.modern-table tbody {
  background: var(--white);
}

.table-row {
  border-bottom: 1px solid rgba(0, 0, 0, 0.05);
  transition: all 0.3s ease;
  animation: fadeInRow 0.6s ease-out both;
}

@keyframes fadeInRow {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.table-row:hover {
  background: linear-gradient(135deg, 
    rgba(16, 185, 129, 0.05) 0%, 
    rgba(6, 182, 212, 0.05) 100%);
  transform: translateX(5px);
  box-shadow: 0 5px 20px rgba(16, 185, 129, 0.1);
}

.modern-table td {
  padding: 20px 24px;
  vertical-align: middle;
  font-size: 0.95em;
}

.user-id {
  font-weight: 700;
  font-size: 1.1em;
  color: #000;
}


.user-info {
  display: flex;
  align-items: center;
  gap: 12px;
}

.user-avatar {
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, var(--accent-orange), var(--pink-accent));
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--white);
  font-weight: 700;
  font-size: 1.1em;
  box-shadow: 0 4px 15px rgba(245, 158, 11, 0.3);
  transition: transform 0.3s ease;
}

.table-row:hover .user-avatar {
  transform: scale(1.1);
}

.username {
  font-weight: 600;
  color: var(--dark-gray);
  font-size: 1em;
}

.user-email {
  color: var(--medium-gray);
  font-weight: 500;
  font-size: 0.95em;
}

.user-address,
.user-phone {
  color: var(--medium-gray);
  font-weight: 500;
  font-size: 0.95em;
}

/* Empty State */
.empty-state {
  text-align: center;
  padding: 80px 40px;
  background: linear-gradient(135deg, 
    rgba(107, 114, 128, 0.05) 0%, 
    rgba(255, 255, 255, 0.95) 100%);
}

.empty-icon {
  width: 80px;
  height: 80px;
  background: linear-gradient(135deg, var(--medium-gray), var(--light-gray));
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--white);
  margin: 0 auto 25px;
  box-shadow: 0 10px 30px rgba(107, 114, 128, 0.2);
  animation: float 4s ease-in-out infinite;
}

.empty-icon svg {
  width: 40px;
  height: 40px;
}

.empty-title {
  font-size: 1.8em;
  font-weight: 700;
  color: var(--dark-gray);
  margin-bottom: 12px;
}

.empty-description {
  font-size: 1.1em;
  color: var(--medium-gray);
  font-weight: 500;
  max-width: 400px;
  margin: 0 auto;
  line-height: 1.6;
}

/* Floating Decorative Shapes */
.floating-shapes {
  position: absolute;
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
  top: 8%;
  right: 5%;
  background: linear-gradient(135deg, var(--accent-orange), var(--pink-accent));
  animation: floatShape 12s ease-in-out infinite;
}

.shape-2 {
  width: 80px;
  height: 80px;
  bottom: 15%;
  left: 8%;
  background: linear-gradient(135deg, var(--success-green), var(--cyan-accent));
  animation: floatShape 8s ease-in-out infinite reverse;
}

.shape-3 {
  width: 60px;
  height: 60px;
  top: 25%;
  left: 15%;
  background: linear-gradient(135deg, var(--accent-purple), var(--primary-blue));
  animation: floatShape 10s ease-in-out infinite;
}

.shape-4 {
  width: 100px;
  height: 100px;
  bottom: 25%;
  right: 12%;
  background: linear-gradient(135deg, var(--cyan-accent), var(--success-green));
  animation: floatShape 15s ease-in-out infinite reverse;
}

@keyframes floatShape {
  0%, 100% { transform: translate(0, 0) rotate(0deg); }
  25% { transform: translate(30px, -25px) rotate(90deg); }
  50% { transform: translate(-20px, -40px) rotate(180deg); }
  75% { transform: translate(-35px, 20px) rotate(270deg); }
}

/* Animation for form elements */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(40px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Responsive Design */
@media (max-width: 1024px) {
  .user-stats-container {
    padding: 40px 30px;
  }
  
  .admin-nav {
    gap: 10px;
  }
  
  .nav-item {
    padding: 10px 16px;
    font-size: 0.9em;
  }
  
  .stats-card {
    padding: 25px;
  }
  
  .table-wrapper {
    overflow-x: auto;
  }
  
  .modern-table {
    min-width: 800px;
  }
}

@media (max-width: 768px) {
  .user-stats {
    padding: 20px 15px;
  }
  
  .user-stats-container {
    padding: 30px 20px;
    border-radius: 24px;
  }
  
  .user-stats-title {
    font-size: 2.2em;
  }
  
  .admin-icon .icon {
    width: 60px;
    height: 60px;
  }
  
  .admin-nav {
    flex-direction: column;
    align-items: center;
    gap: 8px;
  }
  
  .nav-item {
    width: 100%;
    max-width: 200px;
    justify-content: center;
  }
  
  .stats-card {
    max-width: none;
    margin-bottom: 20px;
  }
  
  .table-title {
    font-size: 1.4em;
  }
  
  .modern-table th,
  .modern-table td {
    padding: 16px 20px;
  }
  
  .user-avatar {
    width: 35px;
    height: 35px;
    font-size: 1em;
  }
}

@media (max-width: 480px) {
  .user-stats-container {
    padding: 25px 15px;
    border-radius: 20px;
  }
  
  .user-stats-title {
    font-size: 1.9em;
  }
  
  .user-stats-subtitle {
    font-size: 1.1em;
  }
  
  .admin-nav {
    padding: 15px;
  }
  
  .nav-item {
    padding: 12px 20px;
  }
  
  .stats-card {
    padding: 20px;
    gap: 15px;
  }
  
  .stat-icon {
    width: 50px;
    height: 50px;
  }
  
  .stat-icon svg {
    width: 25px;
    height: 25px;
  }
  
  
  
  .modern-table {
    min-width: 700px;
  }
  
  .modern-table th,
  .modern-table td {
    padding: 12px 16px;
    font-size: 0.9em;
  }
  
  .user-info {
    gap: 10px;
  }
  
  .user-avatar {
    width: 32px;
    height: 32px;
    font-size: 0.9em;
  }
  
  .empty-state {
    padding: 60px 20px;
  }
  
  .empty-icon {
    width: 60px;
    height: 60px;
  }
  
  .empty-icon svg {
    width: 30px;
    height: 30px;
  }
  
  .empty-title {
    font-size: 1.5em;
  }
}

/* Focus States for Accessibility */
.nav-item:focus {
  outline: 3px solid var(--accent-orange);
  outline-offset: 3px;
}

/* Enhanced hover effects */
.user-stats-container:hover .admin-icon {
  transform: scale(1.05);
  transition: transform 0.3s ease;
}

.table-section:hover .table-icon {
  color: var(--pink-accent);
  transform: scale(1.15);
  transition: all 0.3s ease;
}

/* Scroll animations */
.table-row {
  transition: all 0.3s ease;
}

.table-row:nth-child(even) {
  background: rgba(0, 0, 0, 0.02);
}

.table-row:nth-child(even):hover {
  background: linear-gradient(135deg, 
    rgba(16, 185, 129, 0.08) 0%, 
    rgba(6, 182, 212, 0.08) 100%);
}

/* Enhanced loading animation */
.loading-state {
  animation: fadeInUp 0.6s ease-out;
}

/* Custom scrollbar for table */
.table-wrapper::-webkit-scrollbar {
  height: 8px;
}

.table-wrapper::-webkit-scrollbar-track {
  background: var(--light-gray);
  border-radius: 10px;
}

.table-wrapper::-webkit-scrollbar-thumb {
  background: linear-gradient(135deg, var(--accent-orange), var(--pink-accent));
  border-radius: 10px;
}

.table-wrapper::-webkit-scrollbar-thumb:hover {
  background: linear-gradient(135deg, var(--pink-accent), var(--accent-purple));
}
</style>