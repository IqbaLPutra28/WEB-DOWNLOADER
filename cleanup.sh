#!/bin/bash
# Hapus file yang lebih tua dari 60 menit di dalam folder downloads
find /path/to/your/project/backend/downloads -type f -mmin +30 -delete