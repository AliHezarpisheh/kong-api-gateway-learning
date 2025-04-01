# API Gateways

An API gateway is a critical part of any modern technology stack, sitting at the network "edge" of systems and acting as a management tool that mediates between consumers and a collection of back-end services.

- **Routing traffic from a URL to a Back-End system** → Could Provide → Reliability, Observability, and Security.
- **API Gateways** → North-South/Ingress Traffic management → Sitting at the Network Edge.
- **API Gateway** = Control Plane + Data Plane
- API Gateways Use Facade/Adapter Ideas

## API Gateway Diagram

```plaintext
+----------+          +-----------------+        +--------------------+
| Consumer |——(Public Network)——>| API Gateway |——(Private Network)——>| Back-End Services |
+----------+          +-----------------+        +--------------------+
```

### Feature Comparison Table

| Feature             | Reverse Proxy | Load Balancer | API Gateway |
|---------------------|--------------|--------------|-------------|
| Single Back-End    | ✅            | ✅            | ✅           |
| TLS/SSL           | ✅            | ✅            | ✅           |
| Multiple Back-Ends | ❌            | ✅            | ✅           |
| Service Discovery  | ❌            | ✅            | ✅           |
| API Composition    | ❌            | ❌            | ✅           |
| Authorization      | ❌            | ❌            | ✅           |
| Retry Logic        | ❌            | ❌            | ✅           |
| Rate Limiting      | ❌            | ❌            | ✅           |
| Logging & Tracing  | ❌            | ❌            | ✅           |
| Circuit Breaking   | ❌            | ❌            | ✅           |