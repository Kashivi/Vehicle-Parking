<template>
  <div class="login">
    <!-- Background Pattern -->
    <div class="bg-pattern"></div>
    
    <!-- Login Container -->
    <div class="login-container">
      <!-- Header Section -->
      <div class="login-header">
        <div class="parking-icon">
          <svg viewBox="0 0 100 100" class="icon">
            <rect x="10" y="20" width="80" height="60" rx="5" fill="none" stroke="currentColor" stroke-width="3"/>
            <rect x="20" y="30" width="15" height="25" rx="2" fill="currentColor"/>
            <rect x="42.5" y="30" width="15" height="25" rx="2" fill="currentColor"/>
            <rect x="65" y="30" width="15" height="25" rx="2" fill="currentColor"/>
            <text x="50" y="70" text-anchor="middle" font-size="12" fill="currentColor" font-weight="bold">P</text>
          </svg>
        </div>
        <h1 class="login-title">
          <span class="gradient-text">Welcome Back</span>
        </h1>
        <p class="login-subtitle">Access your parking dashboard</p>
      </div>

      <!-- Login Form -->
      <form @submit.prevent="login" class="login-form">
        <div class="form-group">
          <label for="email" class="form-label">
            <svg class="label-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
              <polyline points="22,6 12,13 2,6"/>
            </svg>
            Email Address
          </label>
          <div class="input-wrapper">
            <input 
              type="email" 
              id="email"
              v-model="email" 
              placeholder="Enter your email address" 
              required 
              class="form-input"
            />
            <div class="input-border"></div>
          </div>
        </div>

        <div class="form-group">
          <label for="password" class="form-label">
            <svg class="label-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <rect x="3" y="11" width="18" height="11" rx="2" ry="2"/>
              <circle cx="12" cy="16" r="1"/>
              <path d="M7 11V7a5 5 0 0 1 10 0v4"/>
            </svg>
            Password
          </label>
          <div class="input-wrapper">
            <input 
              type="password" 
              id="password"
              v-model="password" 
              placeholder="Enter your password" 
              required 
              class="form-input"
            />
            <div class="input-border"></div>
          </div>
        </div>

        <button type="submit" class="btn-login">
          <span class="btn-content">
            <svg class="btn-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4"/>
              <polyline points="10,17 15,12 10,7"/>
              <line x1="15" y1="12" x2="3" y2="12"/>
            </svg>
            Sign In
          </span>
          <div class="btn-shimmer"></div>
        </button>
      </form>

      <!-- Error Message -->
      <div v-if="errorMessage" class="error-message">
        <svg class="error-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="12" cy="12" r="10"/>
          <line x1="15" y1="9" x2="9" y2="15"/>
          <line x1="9" y1="9" x2="15" y2="15"/>
        </svg>
        {{ errorMessage }}
      </div>

      <!-- Additional Links -->
      <div class="login-footer">
        <router-link to="/register" class="footer-link">
          Don't have an account? <span class="highlight">Register here</span>
        </router-link>
      </div>

      <!-- Decorative Elements -->
      <div class="floating-shapes">
        <div class="shape shape-1"></div>
        <div class="shape shape-2"></div>
        <div class="shape shape-3"></div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'LoginView',
  data() {
    return {
      email: '',
      password: '',
      errorMessage: ''
    }
  },
  methods: {
    login() {
      axios.post('http://localhost:5000/login', {
        email: this.email,
        password: this.password
      }, {
        headers: { 'Content-Type': 'application/json' }
      })
      .then(res => {
        const data = res.data
        const role = data.role ? data.role.toLowerCase() : null

        localStorage.setItem('auth_token', data.auth_token)
        localStorage.setItem('user', JSON.stringify({
          email: data.email,
          username: data.username,
          role: role,
          user_id: data.user_id
        }))

        if (role === 'admin') {
          this.$router.push('/admin-dashboard')
        } else if (role === 'user') {
          this.$router.push('/user-dashboard')
        } else {
          this.errorMessage = 'Invalid user role'
        }
      })
      .catch(err => {
        this.errorMessage = err.response?.data?.message || 'Network error. Try again.'
        console.error(err)
      })
    }
  }
}
</script>

<style scoped>
/* Color Variables - Vibrant Parking Theme */
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

.login {
  min-height: 100vh;
  background: linear-gradient(135deg, 
    var(--primary-blue) 0%, 
    var(--accent-purple) 25%, 
    var(--pink-accent) 50%, 
    var(--cyan-accent) 75%, 
    var(--success-green) 100%);
  background-size: 400% 400%;
  animation: gradientShift 10s ease infinite;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
  position: relative;
  overflow: hidden;
}

@keyframes gradientShift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

/* Animated Background Pattern */
.bg-pattern {
  position: absolute;
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
  animation: drift 20s linear infinite, pulse 6s ease-in-out infinite;
}

@keyframes drift {
  0% { transform: translate(0, 0) rotate(0deg); }
  100% { transform: translate(30px, 30px) rotate(360deg); }
}

@keyframes pulse {
  0%, 100% { opacity: 0.6; }
  50% { opacity: 1; }
}

/* Login Container */
.login-container {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(15px);
  border-radius: 24px;
  padding: 50px 40px;
  max-width: 450px;
  width: 100%;
  box-shadow: 
    0 25px 80px var(--shadow-dark),
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
    transform: translateY(50px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Header Section */
.login-header {
  text-align: center;
  margin-bottom: 40px;
}

.parking-icon {
  display: inline-block;
  margin-bottom: 20px;
  background: linear-gradient(135deg, var(--cyan-accent), var(--primary-blue), var(--accent-purple));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: float 4s ease-in-out infinite, colorRotate 8s ease infinite;
}

.parking-icon .icon {
  width: 60px;
  height: 60px;
  filter: drop-shadow(0 4px 12px rgba(37, 99, 235, 0.3));
}

@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-8px); }
}

@keyframes colorRotate {
  0%, 100% { filter: drop-shadow(0 4px 12px rgba(37, 99, 235, 0.3)) hue-rotate(0deg); }
  33% { filter: drop-shadow(0 4px 12px rgba(139, 92, 246, 0.3)) hue-rotate(120deg); }
  66% { filter: drop-shadow(0 4px 12px rgba(6, 182, 212, 0.3)) hue-rotate(240deg); }
}

.login-title {
  font-size: 2.5em;
  font-weight: 800;
  margin-bottom: 8px;
  letter-spacing: -1px;
}

.gradient-text {
  background: linear-gradient(135deg, 
    var(--primary-blue) 0%, 
    var(--accent-purple) 30%, 
    var(--pink-accent) 60%, 
    var(--cyan-accent) 100%);
  background-size: 300% 300%;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: textShimmer 4s ease-in-out infinite;
}

@keyframes textShimmer {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}

.login-subtitle {
  color: var(--medium-gray);
  font-size: 1.1em;
  font-weight: 500;
}

/* Form Styling */
.login-form {
  margin-bottom: 30px;
}

.form-group {
  margin-bottom: 25px;
  position: relative;
}

.form-label {
  display: flex;
  align-items: center;
  gap: 8px;
  font-weight: 600;
  color: var(--dark-gray);
  margin-bottom: 8px;
  font-size: 0.95em;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.label-icon {
  width: 18px;
  height: 18px;
  color: var(--primary-blue);
}

.input-wrapper {
  position: relative;
}

.form-input {
  width: 100%;
  padding: 16px 20px;
  border: 2px solid transparent;
  border-radius: 12px;
  background: linear-gradient(var(--white), var(--white)) padding-box,
              linear-gradient(135deg, var(--cyan-accent), var(--primary-blue), var(--accent-purple)) border-box;
  font-size: 1em;
  transition: all 0.3s ease;
  box-shadow: 0 4px 20px var(--shadow);
  outline: none;
  position: relative;
  z-index: 2;
}

.form-input:focus {
  transform: translateY(-2px);
  box-shadow: 0 8px 30px rgba(37, 99, 235, 0.3);
  background: linear-gradient(var(--white), var(--white)) padding-box,
              linear-gradient(135deg, var(--success-green), var(--cyan-accent), var(--accent-orange)) border-box;
}

.form-input::placeholder {
  color: var(--medium-gray);
  opacity: 0.7;
}

.input-border {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 3px;
  background: linear-gradient(90deg, var(--success-green), var(--cyan-accent), var(--accent-orange));
  border-radius: 0 0 12px 12px;
  transition: width 0.3s ease;
}

.form-input:focus + .input-border {
  width: 100%;
}

/* Login Button */
.btn-login {
  width: 100%;
  padding: 18px 24px;
  background: linear-gradient(135deg, 
    var(--primary-blue) 0%, 
    var(--accent-purple) 50%, 
    var(--pink-accent) 100%);
  background-size: 300% 300%;
  color: var(--white);
  border: none;
  border-radius: 12px;
  font-size: 1.1em;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  cursor: pointer;
  transition: all 0.4s ease;
  position: relative;
  overflow: hidden;
  box-shadow: 0 10px 40px rgba(37, 99, 235, 0.4);
  animation: buttonGlow 3s ease-in-out infinite;
}

@keyframes buttonGlow {
  0%, 100% { 
    background-position: 0% 50%;
    box-shadow: 0 10px 40px rgba(37, 99, 235, 0.4);
  }
  50% { 
    background-position: 100% 50%;
    box-shadow: 0 10px 40px rgba(139, 92, 246, 0.6);
  }
}

.btn-content {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  position: relative;
  z-index: 2;
}

.btn-icon {
  width: 20px;
  height: 20px;
  transition: transform 0.3s ease;
}

.btn-shimmer {
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, 
    transparent, 
    rgba(255, 255, 255, 0.2), 
    transparent);
  transition: left 0.6s ease;
  z-index: 1;
}

.btn-login:hover {
  transform: translateY(-3px);
  box-shadow: 0 15px 60px rgba(139, 92, 246, 0.6);
  background-position: 100% 50%;
}

.btn-login:hover .btn-shimmer {
  left: 100%;
}

.btn-login:hover .btn-icon {
  transform: translateX(3px);
}

.btn-login:active {
  transform: translateY(-1px);
}

/* Error Message */
.error-message {
  display: flex;
  align-items: center;
  gap: 10px;
  background: linear-gradient(135deg, rgba(239, 68, 68, 0.1), rgba(236, 72, 153, 0.1));
  border: 2px solid var(--red-accent);
  border-radius: 12px;
  padding: 15px 20px;
  color: var(--red-accent);
  font-weight: 600;
  margin-bottom: 20px;
  animation: shake 0.5s ease-in-out;
}

@keyframes shake {
  0%, 100% { transform: translateX(0); }
  25% { transform: translateX(-5px); }
  75% { transform: translateX(5px); }
}

.error-icon {
  width: 20px;
  height: 20px;
  flex-shrink: 0;
}

/* Footer Links */
.login-footer {
  text-align: center;
  padding-top: 20px;
  border-top: 2px solid rgba(107, 114, 128, 0.1);
}

.footer-link {
  display: block;
  color: var(--medium-gray);
  text-decoration: none;
  margin-bottom: 10px;
  transition: all 0.3s ease;
  font-weight: 500;
}

.footer-link:hover {
  color: var(--primary-blue);
  transform: translateY(-1px);
}

.highlight {
  background: linear-gradient(135deg, var(--accent-orange), var(--pink-accent));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-weight: 700;
}

.forgot-password:hover {
  color: var(--accent-orange);
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
  opacity: 0.1;
}

.shape-1 {
  width: 60px;
  height: 60px;
  top: 10%;
  right: 10%;
  background: linear-gradient(135deg, var(--success-green), var(--cyan-accent));
  animation: floatShape 8s ease-in-out infinite;
}

.shape-2 {
  width: 40px;
  height: 40px;
  bottom: 20%;
  left: 15%;
  background: linear-gradient(135deg, var(--accent-orange), var(--pink-accent));
  animation: floatShape 6s ease-in-out infinite reverse;
}

.shape-3 {
  width: 80px;
  height: 80px;
  top: 60%;
  right: 20%;
  background: linear-gradient(135deg, var(--accent-purple), var(--primary-blue));
  animation: floatShape 10s ease-in-out infinite;
}

@keyframes floatShape {
  0%, 100% { transform: translate(0, 0) rotate(0deg); }
  25% { transform: translate(20px, -15px) rotate(90deg); }
  50% { transform: translate(-10px, -25px) rotate(180deg); }
  75% { transform: translate(-20px, 10px) rotate(270deg); }
}

/* Responsive Design */
@media (max-width: 768px) {
  .login-container {
    padding: 40px 30px;
    margin: 10px;
    max-width: 380px;
  }
  
  .login-title {
    font-size: 2em;
  }
  
  .parking-icon .icon {
    width: 50px;
    height: 50px;
  }
}

@media (max-width: 480px) {
  .login-container {
    padding: 30px 20px;
  }
  
  .login-title {
    font-size: 1.8em;
  }
  
  .form-input {
    padding: 14px 16px;
  }
  
  .btn-login {
    padding: 16px 20px;
  }
}

/* Focus States for Accessibility */
.btn-login:focus,
.form-input:focus {
  outline: 3px solid var(--accent-orange);
  outline-offset: 2px;
}

/* Loading State */
.btn-login:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  animation: none;
}

/* Form Animation */
.login-form {
  animation: fadeInUp 0.8s ease-out 0.2s both;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Interactive Hover Effects */
.login-container:hover .parking-icon {
  transform: scale(1.1);
  transition: transform 0.3s ease;
}

.form-group:hover .label-icon {
  color: var(--accent-orange);
  transform: scale(1.1);
  transition: all 0.3s ease;
}
</style>