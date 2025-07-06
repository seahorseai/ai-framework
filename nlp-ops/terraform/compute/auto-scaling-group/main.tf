provider "aws" {

  region = "eu-south-2"

}


resource "aws_launch_template" "template" {
  
  name_prefix     = "test"
  
  image_id        = "ami-0ae0f14cea4998f46"
  
  instance_type   = "t3.micro"
}

resource "aws_autoscaling_group" "autoscale" {

  name                  = "test-autoscaling-group"  

  desired_capacity      = 3

  max_size              = 6

  min_size              = 3

  health_check_type     = "EC2"

  termination_policies  = ["OldestInstance"]

  vpc_zone_identifier   = ["subnet-0c48daf785f075d71, subnet-03480dd5fc67e27f7, subnet-0ca1e78832b4e3941"]

  

  health_check_grace_period = 300


  launch_template {

    id      = aws_launch_template.template.id

    version = "$Latest"

  }

  # lifecycle { 

  #   ignore_changes = [desired_capacity]

  # }

}


resource "aws_autoscaling_policy" "scale_down" {

  name                   = "test_scale_down"

  autoscaling_group_name = aws_autoscaling_group.autoscale.name

  adjustment_type        = "ChangeInCapacity"

  scaling_adjustment     = -1

  cooldown               = 120

}



resource "aws_cloudwatch_metric_alarm" "scale_down" {

  alarm_description   = "Monitors CPU utilization"

  alarm_actions       = [aws_autoscaling_policy.scale_down.arn]

  alarm_name          = "test_scale_down"

  comparison_operator = "LessThanOrEqualToThreshold"

  namespace           = "AWS/EC2"

  metric_name         = "CPUUtilization"

  threshold           = "25"

  evaluation_periods  = "5"

  period              = "30"

  statistic           = "Average"



  dimensions = {

    AutoScalingGroupName = aws_autoscaling_group.autoscale.name

  }

}
