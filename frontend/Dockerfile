# Use official Node.js image
FROM node:20

# Set working directory
WORKDIR /app/frontend

# Copy package.json and install dependencies
COPY package*.json ./
RUN npm install

# Copy project files
COPY . .

# Expose port 3000
EXPOSE 3000

# Start React app
CMD ["npm", "start"]
