from pydantic import BaseModel, Field


class NetworkInput(BaseModel):
    duration: int = Field(..., ge=0, description="Connection duration in seconds")
    protocol_type: str = Field(..., description="Protocol type: tcp, udp, icmp")
    service: str = Field(..., description="Network service: http, ftp, smtp etc.")
    flag: str = Field(..., description="Connection status flag: SF, S0, REJ etc.")
    src_bytes: int = Field(..., ge=0, description="Bytes sent from source")
    dst_bytes: int = Field(..., ge=0, description="Bytes sent to destination")
    land: int = Field(..., ge=0, le=1, description="1 if src/dst same host/port")
    wrong_fragment: int = Field(..., ge=0, description="Number of wrong fragments")
    urgent: int = Field(..., ge=0, description="Number of urgent packets")
    hot: int = Field(..., ge=0, description="Number of hot indicators")
    num_failed_logins: int = Field(..., ge=0, description="Failed login attempts")
    logged_in: int = Field(..., ge=0, le=1, description="1 if logged in successfully")
    num_compromised: int = Field(..., ge=0, description="Compromised conditions")
    root_shell: int = Field(..., ge=0, le=1, description="1 if root shell obtained")
    su_attempted: int = Field(..., ge=0, description="Su root command attempted")
    num_root: int = Field(..., ge=0, description="Root accesses")
    num_file_creations: int = Field(..., ge=0, description="File creation operations")
    num_shells: int = Field(..., ge=0, description="Shell prompts")
    num_access_files: int = Field(..., ge=0, description="Access control files")
    num_outbound_cmds: int = Field(..., ge=0, description="Outbound commands in ftp")
    is_host_login: int = Field(..., ge=0, le=1, description="1 if host login")
    is_guest_login: int = Field(..., ge=0, le=1, description="1 if guest login")
    count: int = Field(..., ge=0, description="Connections to same host last 2 sec")
    srv_count: int = Field(..., ge=0, description="Connections to same service last 2 sec")
    serror_rate: float = Field(..., ge=0.0, le=1.0, description="SYN error rate")
    srv_serror_rate: float = Field(..., ge=0.0, le=1.0, description="SYN error rate by service")
    rerror_rate: float = Field(..., ge=0.0, le=1.0, description="REJ error rate")
    srv_rerror_rate: float = Field(..., ge=0.0, le=1.0, description="REJ error rate by service")
    same_srv_rate: float = Field(..., ge=0.0, le=1.0, description="Same service rate")
    diff_srv_rate: float = Field(..., ge=0.0, le=1.0, description="Different service rate")
    srv_diff_host_rate: float = Field(..., ge=0.0, le=1.0, description="Different host rate")
    dst_host_count: int = Field(..., ge=0, le=255, description="Destination host count")
    dst_host_srv_count: int = Field(..., ge=0, le=255, description="Dst host service count")
    dst_host_same_srv_rate: float = Field(..., ge=0.0, le=1.0, description="Dst host same service rate")
    dst_host_diff_srv_rate: float = Field(..., ge=0.0, le=1.0, description="Dst host diff service rate")
    dst_host_same_src_port_rate: float = Field(..., ge=0.0, le=1.0, description="Dst host same src port rate")
    dst_host_srv_diff_host_rate: float = Field(..., ge=0.0, le=1.0, description="Dst host srv diff host rate")
    dst_host_serror_rate: float = Field(..., ge=0.0, le=1.0, description="Dst host SYN error rate")
    dst_host_srv_serror_rate: float = Field(..., ge=0.0, le=1.0, description="Dst host srv SYN error rate")
    dst_host_rerror_rate: float = Field(..., ge=0.0, le=1.0, description="Dst host REJ error rate")
    dst_host_srv_rerror_rate: float = Field(..., ge=0.0, le=1.0, description="Dst host srv REJ error rate")

    class Config:
        json_schema_extra = {
            "example": {
                "duration": 0,
                "protocol_type": "tcp",
                "service": "http",
                "flag": "SF",
                "src_bytes": 232,
                "dst_bytes": 8153,
                "land": 0,
                "wrong_fragment": 0,
                "urgent": 0,
                "hot": 0,
                "num_failed_logins": 0,
                "logged_in": 1,
                "num_compromised": 0,
                "root_shell": 0,
                "su_attempted": 0,
                "num_root": 0,
                "num_file_creations": 0,
                "num_shells": 0,
                "num_access_files": 0,
                "num_outbound_cmds": 0,
                "is_host_login": 0,
                "is_guest_login": 0,
                "count": 5,
                "srv_count": 5,
                "serror_rate": 0.2,
                "srv_serror_rate": 0.2,
                "rerror_rate": 0.0,
                "srv_rerror_rate": 0.0,
                "same_srv_rate": 1.0,
                "diff_srv_rate": 0.0,
                "srv_diff_host_rate": 0.0,
                "dst_host_count": 30,
                "dst_host_srv_count": 255,
                "dst_host_same_srv_rate": 1.0,
                "dst_host_diff_srv_rate": 0.0,
                "dst_host_same_src_port_rate": 0.03,
                "dst_host_srv_diff_host_rate": 0.04,
                "dst_host_serror_rate": 0.03,
                "dst_host_srv_serror_rate": 0.01,
                "dst_host_rerror_rate": 0.0,
                "dst_host_srv_rerror_rate": 0.01
            }
        }


class PredictionResponse(BaseModel):
    attack_type: str = Field(
        ...,
        description="Predicted attack class: Normal, DoS, Probe, R2L, U2R"
    )
    confidence: float = Field(
        ...,
        description="Model confidence score (0.0 to 1.0)"
    )
    description: str = Field(
        ...,
        description="Plain English explanation of the detected threat"
    )