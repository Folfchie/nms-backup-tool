# nms-backup-tool
A simple Python script that I use to automate No Man's Sky save backups.

## Dependencies
Requires Python 3.6+ (PEP 498)

## Installation
* Download the latest release
* Extract the ZIP archive
* Run `nms-backup-tool.py` from a terminal, or use cron/task scheduler to automate it

## Usage
```
python3 ./nms-backup-tool.py -i {sourceDirectory} -o {destinationDirectory}
```

### Options
```
-h    Show help dialogue
-i    Source directory, must be an absolute path, can be a file or directory
-o    Destination directory, must be an absolute path, can be a file or directory
-s    Silent mode, suppresses console output
-s    Autosave, enables automatic backup
```

## Behavior
```mermaid
flowchart TD
    A[Start nms-backup-tool] --> B[Parse CLI arguments]

    B --> C{Silent mode?}
    C -->|Yes| D[Suppress console output]
    C -->|No| E[Continue]
    D --> E

    E --> F[Start backup]
    F --> G[Inspect source path]

    G --> H{Source is a directory?}
    H -->|Yes| I[Find all .hg files]
    H -->|No| J{Source is an .hg file?}

    J -->|Yes| K[Add file to backup set]
    J -->|No| X[Backup failed]

    I --> L{Valid .hg files found?}
    K --> L

    L -->|No| X
    L -->|Yes| M{Destination is a directory?}

    M -->|No| X
    M -->|Yes| N[Create timestamped backup directory]

    N --> O[Copy .hg files with metadata]
    O --> P{Multiple .hg files?}

    P -->|Yes| Q[Create ZIP archive]
    Q --> R[Remove temporary backup directory]

    P -->|No| S[Keep timestamped backup directory]
    R --> T[Backup complete]
    S --> T

    T --> U{Autosave enabled?}

    U -->|No| V[Exit successfully]
    U -->|Yes| W[Wait configured interval]
    W --> F

    X --> Y[Exit with failure status]
```