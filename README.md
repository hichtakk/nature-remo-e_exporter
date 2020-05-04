# nature-remo-e_exporter

[![container repository](https://img.shields.io/badge/docker-0.1.0-blue)](https://hub.docker.com/repository/docker/hichtakk/nature-remo-e-exporter) 

Prometheus exporter for Nature REMO E (Lite) energy monitoring device.  
https://nature.global/jp/nature-remo-e


```
docker run -d -e CLOUD_API_TOKEN=${YOUR_TOKEN} -p 18001:18001 hichtakk/nature-remo-e-exporter:0.1.0
```